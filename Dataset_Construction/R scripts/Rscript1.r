args = commandArgs(trailingOnly=TRUE)
#command to run:    Rscript Rscript1.r 'sample_file' 'Gene_locs_file' 'output_location'
#command to run (from Dataset_Construction folder):    Rscript R\ scripts/Rscript1.r Workspace/4_FASTA_FILES/HG00614_19.fa.gz Gene_locs.txt Workspace/5_GENE_FASTA_FILES/ 19

library(ShortRead)

f<-args[1]   #those are created from previous step, or from other pipelines
genes<-read.table(args[2], as.is=T) # this file contains the chromosome/positions for the genes of interest


fa<-readFasta(f)

chr<-args[4]
name<-gsub(".fa.gz", "",f)
smp<-strsplit(basename(name), chr)
smp<-strsplit(smp[[1]], "_")
smp<-paste(smp[[1]],collapse='_')

print("Loaded Sample")

curgenes<-genes[genes[,2]==chr,]
print(curgenes)


SEQ_HERE<-as.character(DNAString(as.character(sread(fa))))

for(i in 1:length(curgenes[,1])){
	
	
	
	if (nchar(SEQ_HERE)>=700){
		seq<-as.character(DNAString(as.character(sread(fa)))[curgenes[i,3]:curgenes[i,4]]) ## Isolate location of gene in chromosome, start-stop
		newseq<-ShortRead(sread=DNAStringSet(seq), id=BStringSet(paste0(smp, "_", curgenes[i,1], "_", curgenes[i,2], "_", curgenes[i,3], "_", curgenes[i,4]))) # prepare fasta sequence
		writeFasta(newseq, paste0(args[3],smp, "_", curgenes[i,1], ".fa")) # write it out
		}

	else{
		seq<-as.character(paste(rep('N',607),collapse='')) ## Isolate location of gene in chromosome, start-stop
		newseq<-ShortRead(sread=DNAStringSet(seq), id=BStringSet(paste0(smp, "_", curgenes[i,1], "_", curgenes[i,2], "_", curgenes[i,3], "_", curgenes[i,4])))
		writeFasta(newseq, paste0(args[3],smp, "_", curgenes[i,1], ".fa")) # write it out
		}
	
		}