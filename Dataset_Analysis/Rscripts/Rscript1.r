args = commandArgs(trailingOnly=TRUE)
#command to run (from Dataset_Analysis folder):    Rscript Rscripts/Rscript1.r /Workspace/2_DATASETS/FR_FULL_NEW_DATA_MODIFIED_AA.fa-Fontana_Ranuccio Workspace/1_OG_Dataset/FR_FULL_NEW_DATA_MODIFIED_AA.fa
library(ShortRead)


directory=args[1] #The directory location for the new folders to be created 

# This correspond to the protein sequences for the reference samples
fa<-readAAStringSet(args[2]) #GET it from 1_OG_DATASET

mainDir<-getwd() #get current dir, assumes output dir is a subfodler!
setwd(file.path(mainDir,directory))
genes<-readLines("Genes.txt") #In the 2_DATASETS appropriate folder 
samples<-readLines("Samples.txt") #In the 2_DATASETS appropriate folder 


mainDir <- getwd()


for(i in 1:length(genes)){
	
	
	subDir <- genes[i]
	dir.create(file.path(mainDir, subDir), showWarnings = FALSE) # Create Gene specific subfolder

	d<-file.path(mainDir,genes[i])
	setwd(d)
	
	FASTA_ENTRIES_WITH_GENE=c()
	for( N in 1:length(names(fa))){
		NAME_HERE=names(fa)[N]
		NAME_HERE=strsplit(NAME_HERE,'/', fixed=T)[[1]][1]
		NAME_HERE=strsplit(NAME_HERE,'_', fixed=T)
		NAME_HERE=NAME_HERE[[1]][length(NAME_HERE[[1]])]
		
		if(NAME_HERE==genes[i]){
			FASTA_ENTRIES_WITH_GENE=c(FASTA_ENTRIES_WITH_GENE,N)
			}
		
		}
	
	
	
	curfa<-fa[FASTA_ENTRIES_WITH_GENE]  ### biostring with only one gene (all fasta seqs that have the gene name in their name), all sample sequences tied with their sample name
	####grep to select only AMELX not AMELX2 paste0(genes[i],'\/','[1-9]+','$'
	
	
	#### Isolate Selected Ancient Samples from modern
	AS=c() #List of ancient samples, to be filled
	All_Sample_Names=c() ### sperate names of samples into a different list
	for(ZNM in names(curfa)){
		nm_here=strsplit(ZNM,'_') #split sample name from protein name
		nm_here=nm_here[[1]][-length(nm_here[[1]])]
		nm_here=paste(nm_here, collapse = '_')
		
		All_Sample_Names=c(All_Sample_Names,nm_here)
	}
	
	
	#### Isolate ancient samples from modern ones into their own dataset
	for (S in samples){
		AS=c(AS,which(All_Sample_Names==S))
		}
	
	
	
	
	
	
	
	#Corrections of unusable characters
	for (SMPL in 1:length(curfa)){
	
		SEQ_HERE=as.character(curfa[SMPL])
		SEQ_HERE=gsub('X','?',SEQ_HERE)
		curfa[SMPL]=SEQ_HERE
	
	
		}
	
	
	
	cursa<-curfa[AS]
	curva<-curfa[-AS]

	
	##### Remove Duplicate entries
	curfa=curfa[!duplicated(names(curfa))]
	cursa=cursa[!duplicated(names(cursa))]
	curva=curva[!duplicated(names(curva))]
	
	

	writeXStringSet(curfa, paste0(genes[i], "_o.fa"))
	writeXStringSet(cursa, paste0(genes[i], "_ancient.fa"))
	writeXStringSet(curva, paste0(genes[i], "_no_ancient.fa"))
	
}
