#command to run:    Rscript Rscript4.r  Directory
#command to run (from Dataset_Construction folder):    Rscript Rscripts/Rscript4.r /Workspace/2_DATASETS/New_Ref_Seq_3_21_1846.fa-H_antecessor-1846

args = commandArgs(trailingOnly=TRUE)


library("phyclust")

directory<-args[1]

mainDir<-getwd() #get current dir, assumes output dir is a subfodler!
setwd(file.path(mainDir,directory))


genes<-readLines("Genes.txt")

if(file.exists(paste0(file.path(mainDir,directory),"/Concatenated_Proteins.txt"))){
    
    genes<-readLines("Concatenated_Proteins.txt")


}







for(g in 1:length(genes)){

    setwd(file.path(mainDir,directory,genes[g]))
    fasta_data=read.fasta(paste0("./",genes[g],"_aln_e.fa"), code.type ="AMINO_ACID",aligned=TRUE)
    names=fasta_data$seqname
    
    for (i in 1:length(names)){
        names[i]=paste0(substring(names[i], 1, nchar(names[i])),"\t")
    }


    write.phylip( fasta_data$org , paste0("./",genes[g],"_aln_e.phy") ,code.type = "AMINO_ACID",seqname=names, width.seqname =100)

# backup method if errors
# write.phylip.format( fasta_data$org.code , paste0("./",genes[g],"_aln_e.phy"),seqname=names, width.seqname =10)
}



######### Turn the concatenated one into Phyl as well


setwd(file.path(mainDir,directory,'CONCATINATED'))
concat_fasta=read.fasta("CONCATINATED_o.fa", code.type ="AMINO_ACID",aligned=TRUE)


names=concat_fasta$seqname 
for (i in 1:length(names)){
    names[i]=paste0(substring(names[i], 1, nchar(names[i])),"\t")
}

write.phylip( concat_fasta$org , "./CONCATINATED_aln_e.phy" ,code.type = "AMINO_ACID",seqname=names, width.seqname =100)
