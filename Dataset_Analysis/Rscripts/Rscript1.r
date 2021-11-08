args = commandArgs(trailingOnly=TRUE)
#command to run:    Rscript Rscript1.r OutputDir REF_dataset 
#command to run (from Dataset_Construction folder):    Rscript Rscripts/Rscript1.r /Workspace/2_DATASETS/New_Ref_Seq_3_21_1846.fa-1846 Workspace/1_OG_Dataset/New_Ref_Seq_3_21_1846.fa
library(ShortRead)


directory=args[1] #The directory location for the new folders to be created 

# This correspond to the protein sequences for the reference samples
fa<-readAAStringSet(args[2]) #GET it from 1_OG_DATASET

mainDir<-getwd() #get current dir, assumes output dir is a subfodler!
setwd(file.path(mainDir,directory))
genes<-readLines("Genes.txt") #In the 2_DATASETS appropriate folder 


mainDir <- getwd()

for(i in 1:length(genes)){
	
	
	subDir <- genes[i]
	dir.create(file.path(mainDir, subDir), showWarnings = FALSE) # Create Gene specific subfolder

	d<-file.path(mainDir,genes[i])
	setwd(d)
	curfa<-fa[grep(genes[i], names(fa))]  ### biostring with only one gene (all fasta seqs that have the gene name in their name), all sample sequences tied with their sample name
	
	
	#Corrections of unusable characters
	for (SMPL in 1:length(curfa)){
	
		SEQ_HERE=as.character(curfa[SMPL])
		SEQ_HERE=gsub('X','?',SEQ_HERE)
		curfa[SMPL]=SEQ_HERE
	
	
		}
	
	

	writeXStringSet(curfa, paste0(genes[i], "_o.fa")) 
}
