args = commandArgs(trailingOnly=TRUE)

#command to run:    Rscript Rscript2.r WorkingDir  
#command to run (from Dataset_Construction folder):    Rscript Rscripts/Rscript2.r /Workspace/2_DATASETS/New_Ref_Seq_3_21_1846.fa-H_antecessor-1846


library(ShortRead)

directory<-args[1] #The directory location for the new folders to be created 
mainDir<-getwd() #get current dir, assumes output dir is a subfodler!
setwd(file.path(mainDir,directory))
genes<-readLines("Genes.txt") #In the 2_DATASETS appropriate folder 

Samples<-readLines("Samples.txt")






## Info output
################################################################################################################################
# 0 sample name
# 0.1 gene name
# 1. total number of sites in aln
# 2. total number of non-missing sites in the ancient sample
# 3. number of seg. sites in aln
# 4. number of seg. sites in the ancient sample
# 5. number of seg.&non-singletons sites in aln (here singleton means a seg site where only one sample has a difference)
# 6. number of seg-&non-singletons sites in the ancient sample (here singleton means a seg site where only one sample has a difference)
# 7. number of seg. sites where the ancient sample has a unique site









#################################################################
##SET UP FUNCTIONS

is.integer0 <- function(x){
  is.integer(x) && length(x) == 0L
}

GetNotInfoPos<-function(x){
x<-x[x=="X" | x=="-" | x=="?"]
return(length(x))
}

GetSegSites<-function(x){
return(length(unique(x[as.character(x)!="-" & as.character(x)!="X" & as.character(x)!="?"])))
}


GetSingletons<-function(x){
if(length(unique(x[as.character(x)!="-" & as.character(x)!="X" & as.character(x)!="?" ] ))==1){
    return(0)
}else if(length(unique(x[as.character(x)!="-" & as.character(x)!="X" & as.character(x)!="?" ]))==2){
    if((table(x[as.character(x)!="-" & as.character(x)!="X" & as.character(x)!="?" ])[1]==1) |(table(x[as.character(x)!="-" & as.character(x)!="X" & as.character(x)!="?" ])[2]==1)){
        return(1)
    }else{
        return(0)
}
}else{
return(0)
}
}


GetAncientUnique<-function(x, aid){
    if(length(unique(x))>1){
        if(sum(x==x[aid])==1){
             return(1)
        }else{
              return(0)
        }
    }else{
          return(0)
    }
}


###############################################################################
###### FUNCTIONS END






















print("Moving to I,L switching")
#######################################################################################################################################################################################################################################
#####Switch Animo Acids I and L




#### Convert all gaps of ancient sample to '?', for better phylogenetic analysis
CONVERT_GAPS_TO_MISSING=1


for(g in 1:length(genes)){              #### for every gene
    setwd(file.path(mainDir,directory, genes[g]))   ### go to the dir
    
    f<-paste0(genes[g], "_aln.fa")       ## grab the aligned fasta file
    fa<-readAAStringSet(f)               ## get it as a biostring
    
    fatabble<-as.matrix(t(as.data.frame(strsplit(as.character(fa), ""))))  # transform it to a matrix
    
    
    Jsites<-c() #find sites that have an I or an L for any of the ancient sites and keep them here
    
    
    
    
    for (K in Samples){ # Cycle through samples
        aid<-grep(K, names(fa))
		print(c(genes[g],K))

		
		
		
        if (is.integer0(K)==FALSE){ #if current sample does have this gene, 
            Jsites<-c(Jsites,which(fatabble[aid,]=="I" | fatabble[aid,]=="L"))    # find which sites of sample have either an I or L, append them to Jsites
            sam=K #keep that sample for later
			}
    
	
		if (CONVERT_GAPS_TO_MISSING==TRUE){
			Gapsites<-which( fatabble[aid,]=="_" | fatabble[aid,]=="-" | fatabble[aid,]=="X" | fatabble[aid,]=="." )
			fatabble[aid,Gapsites]='?'
			
			}
	
	
	
	
	}
    
    
    
    
    
    
    fafaketabble=fatabble #dataset with only one ancient sample! To be used next
    for (non_sam in Samples){ # Creation fo the above mentioned dataset
        if (non_sam!=sam){
            To_Remove=grep(non_sam,row.names(fafaketabble))
    
            if (is.integer0(To_Remove)==FALSE){
                fafaketabble=fafaketabble[-To_Remove,]

            }
        }
    }
    
    
    
    
    
    print(fatabble[aid,Gapsites])
	
    if(length(Jsites)>0 ){   
    
        for(s in 1:length(Jsites)){ #for every one of these sites
            cursite<-fatabble[,Jsites[s]] # OG curious sites
            
            fakecursite<-fafaketabble[,Jsites[s]] # curious sites, after removing all ancient samples but one (so we can assess the sites only using modern samples)
            
            optssite<-as.character(fakecursite[-grep(sam, names(cursite))])
            
            
            if(length(table(optssite[optssite=="L" | optssite=="I"]))==1){
                cursite[cursite=="L" | cursite=="I"]<-names(table(optssite[optssite=="L" | optssite=="I"]))
            }else{
                cursite[cursite=="L" | cursite=="I"]<-"L"
            }
            fatabble[,Jsites[s]]<-cursite
            
        }
            
           
        newseq<-apply(fatabble, 1, paste, collapse="")
        names(newseq)<-names(fa)
        writeXStringSet(AAStringSet(newseq), gsub(".fa", "_e.fa", f))
        }
    
    
    else{
		newseq<-apply(fatabble, 1, paste, collapse="")
		names(newseq)<-names(fa)
        writeXStringSet(AAStringSet(newseq), gsub(".fa", "_e.fa", f))
    }
}



##############################################################################################


###### GET INFO

for (sam in Samples){ # Generate the Info for each ancient Sample (Seg sites, Singletons etc)
    tab<-NULL
    for(g in 1:length(genes)){
            setwd(file.path(mainDir,directory, genes[g]))
            f<-paste0(genes[g], "_aln_e.fa")
            
            fa<-readAAStringSet(f)

            fatabble<-as.matrix(t(as.data.frame(strsplit(as.character(fa), ""))))

            
            # When you have multiple ancient samples, you should analyse them one by one. So lets remove the rest of them, if they exist for analysing this one
            for (non_sam in Samples){
                if (non_sam!=sam){
                    To_Remove=grep(non_sam,row.names(fatabble))

                    if (is.integer0(To_Remove)==FALSE){
                        fatabble=fatabble[-To_Remove,]
                        fa=fa[-To_Remove]
                        }
                }
            }
            
            
            fanonmissing<-fatabble[,(fatabble[grep(sam, names(fa)),]!="-" & fatabble[grep(sam, names(fa)),]!="X" & fatabble[grep(sam, names(fa)),]!="?" )]

            if(is.null(dim(fanonmissing))!=TRUE){
				if (dim(fanonmissing)[2]>0){
					## total sites
					TotalSites<-dim(fatabble)[2]
					SitesAncient<-dim(fanonmissing)[2]
					
					
					##seg sites
					ss<-apply(fatabble, 2, GetSegSites)
					SegSites<-length(ss[ss>1])
					ss<-apply(fanonmissing, 2, GetSegSites)
					SegSitesAncient<-length(ss[ss>1])
					
					#singletons
					ss<-apply(fatabble, 2, GetSingletons)
					NonSingSites<-SegSites-length(ss[ss==1])
					ss<-apply(fanonmissing, 2, GetSingletons)
					NonSignAncient <-SegSitesAncient-length(ss[ss==1])
					
					#ancient unique
					AncientUnique<-sum(apply(fanonmissing, 2, GetAncientUnique, grep(sam, names(fa)))==1)
					tab<-rbind(tab, c(sam, genes[g], TotalSites, SitesAncient, SegSites, SegSitesAncient, NonSingSites, NonSignAncient, AncientUnique, f))
					}
                
            }
            else{
                message("Error - Not enough Site for Sample found")
                }
        }

    setwd(file.path(mainDir,directory))

    colnames(tab)<-c("Sample_name", "Gene_name", "Total_sites", "Sites_in_ancient", "Segregating_sites", "a_Segregating_sites", "Non_singletons", "a_Non_singletons", "Unique_ancient_sites", "File_name")

    #change name here:
    write.table(tab, file=paste0("Alignments_info_","Sample_",sam,".txt"), col.names=T, row.names=F, quote=F, sep="\t")
}
#######################################################################################################################################################################################################################################



