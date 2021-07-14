#--args $HOME_DIR $SAMPLE_NAME $COMPLETENESS_CUTOFF;
#command to run:    Rscript Rscript3.r  
#command to run (from Dataset_Construction folder):    Rscript Rscripts/Rscript3.r /Workspace/2_DATASETS/New_Ref_Seq_3_21_1846.fa-H_antecessor-1846 K 0.3


args = commandArgs(trailingOnly=TRUE)


#########################################################################################################################################################################
#### Set up



library(ShortRead)
library("stringr")
library(data.table)

f_dowle = function(dt, x) {
        na.replace = function(v,value=x) { v[is.na(v)] = value; v }
        for (i in names(dt))
        eval(parse(text=paste("dt[,",i,":=na.replace(",i,")]")))
    }
    


directory=args[1]
mainDir<-getwd() #get current dir, assumes output dir is a subfodler!
setwd(file.path(mainDir,directory))

genes<-readLines("Genes.txt") #In the 2_DATASETS appropriate folder 

Samples<-readLines("Samples.txt")














#########################################################################################################################################################################
#### Filter proteins (optional)





CUTOFF=TRUE # Flag to use protein coverage cutoff

if (CUTOFF==TRUE){ # This loop cycles through the genes. If any of the samples pass the provided cutoff coverage for that gene, it will be included in the analysis. If all samples don't have the desired cutoff, they are rejected!
    
    genes=c()


    for (sam in Samples){
        gene_file=read.table(paste0("Alignments_info_","Sample_",sam,".txt"),header=TRUE,sep="\t")
        
        for (i in 1:dim(gene_file)[1]){
            COMPLETENESS= (as.numeric(gene_file[i,4]) / as.numeric(gene_file[i,3]))
        
            if (COMPLETENESS>=as.numeric(args[3])){
                genes=c(genes,as.character(gene_file[i,2]))
                print(paste0("Acceptable Gene: ",as.character(gene_file[i,2])," with missingness: ",as.character(1-COMPLETENESS)))
            }

        }
    
    }
    genes=unique(genes)
    print("Acceptable Genes, above cut off")
    print(genes)
}


write(genes, file = "Concatenated_Proteins.txt")
print(as.numeric(args[3]))














#########################################################################################################################################################################
#### Concatenation


ALL_NAMES=c()
CONC=c()
LENGTH=0
for(g in 1:length(genes)){   

    setwd(paste0(directory,genes[g]))
    fasta_here<-readAAStringSet(paste0("./",genes[g],"_aln_e.fa"))
    
###################################################### To gather all names, from all fasta
    NAMES=names(fasta_here)
    
    for (J in 1:length(NAMES)){
        STR=str_split(NAMES[J],"_")                         #to fix names
        NAMES[J]=paste(head(STR[[1]],-1),collapse="_")
    }

    ALL_NAMES=c(ALL_NAMES,NAMES)
    names(fasta_here)=NAMES
#####################################################

    print(genes[g])
    if (length(CONC)!=0){ ##this runs after the first loop
    
        CONCHERE=data.table(as.matrix(fasta_here), keep.rownames = TRUE) ##new gene to add
        
        
        CONC=data.table(CONC) ### previous concat genes
        CONC<-merge(CONC, CONCHERE, by="rn", all=TRUE) #merge em
        # RND_COL_NAMES=sample(1:999999, length(colnames(CONC))-1, replace=F) ### because merging dataframes sucks-a if they have the same column names
        RND_COL_NAMES=seq(1:(length(colnames(CONC))-1)) ### because merging dataframes sucks-a if they have the same column names
        
        
        for (C in 1:length(RND_COL_NAMES)){              ### so we randomize the column names after we join them, so they are for sure different from the other data.frame to be merged
           
           RND_COL_NAMES[C]=paste0("C",as.character(RND_COL_NAMES[C]))
           
        }
        
        colnames(CONC)[2:length(CONC)]=RND_COL_NAMES     ### change all column names with the random ones except the first which is "rn" for row names
        
        
        LENGTH=LENGTH+length(CONCHERE)
        print(length(CONC)) ##keep track of length and which gene we are on
        print(LENGTH)
        print("------")
    }

    else{ #this runs in the first loop
        
        CONC=data.table(as.matrix(fasta_here), keep.rownames = TRUE) ##in this we will concatinate all genes
    
        LENGTH=LENGTH+length(CONC)
        print(length(CONC)) ##keep track of length and which gene we are on
        print(LENGTH)
        print("------")
    }
    
}

###Some formating fixes
ALL_NAMES=ALL_NAMES[!duplicated(ALL_NAMES)] ##here are all the unique names
CONC=data.table(CONC) 
f_dowle(CONC, "X")


















############################################################################################################################################################################
#### Masking of Samples Optional, should require a list to do so. If TRUE, runs

MASKED=1
MASKED_SAMPS=c()

if (MASKED==TRUE){
    
    MASKED_SAMPS=c("Gorilla-gorilla","HUMAN","Pan_troglodytes","Pongo_abelii")
    ANC_SAMPL=args[2]
    ANC_SAMPL=CONC[which(CONC[,1]==ANC_SAMPL)]
    MISSING=which(ANC_SAMPL[,]=="-" | ANC_SAMPL[,]=="\\?" | ANC_SAMPL[,]=="X" )
    
    
    for (SMPL in 1:length(MASKED_SAMPS)){
        
        MASKED_SAMPLE=CONC[which(CONC[,1]==MASKED_SAMPS[SMPL])]
        MASKED_SAMPLE[,1]=paste0("MASKED_",as.character(MASKED_SAMPLE[,1]))
        MASKED_SAMPLE[,MISSING]="-"
        CONC=rbind(CONC,MASKED_SAMPLE)
        
    }
    
    
}











############################################################################################################################################################################
####Get missingess of each sample, add it to their label


PRINT_MISSINGNESS=1


if (PRINT_MISSINGNESS==TRUE){


    for (J in 1:dim(CONC)[1]){


        TOTAL=dim(CONC)[2]-1   #length of full sequence - 1 so we count the label as well
        MISS=sum(str_count(as.character(CONC[J]),"-")) + sum(str_count(as.character(CONC[J]),"X")) + sum(str_count(as.character(CONC[J]),"//?"))  ##count missing positions

        PERC_MISS=(MISS/TOTAL) #get missingness as a percentage
        PERC_COMPLET=1-PERC_MISS   #get completeness as a percentage
        PERC_COMPLET=format(round(PERC_COMPLET, 2), nsmall = 2) ##fix decimal number 
        CONC[J][[1]]=paste0(CONC[J][[1]],"-",PERC_COMPLET)   #change name to include completeness
        print(CONC[J][[1]]) #check new name

    }
    
}
















############################################################################################################################################################################
####Final format, output


FINAL_SEQ<-apply(CONC[ ,!"rn"], 1, paste, collapse="")

FINAL_SEQ<-AAStringSet(FINAL_SEQ)
names(FINAL_SEQ)<-CONC$rn


setwd(directory)
writeXStringSet(FINAL_SEQ, "CONCATINATED_o.fa")


#Finito



