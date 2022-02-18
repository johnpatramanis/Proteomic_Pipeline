args = commandArgs(trailingOnly=TRUE)
#command to run:    Rscript Rscript1.r 'sample_file' 'Starts_file' 'EIT_folder_location' 'output_location'
#command to run(from Dataset_Construction folder):    Rscript R\ scripts/Rscript3.r Workspace/8_BLASTED_GENES/DENISOVA_DENISOVA_ADNA_FRMT_AMELX_spliced.blast Workspace/PROTEINS_FASTAS/

library(ShortRead)


fas<-args[1]


#Get gene and sample name

name<-gsub(".blast", "", fas)
name<-strsplit(basename(name), "_FRMT_")
gene<-name[[1]][2]
gene<-name[[1]][2]<-gsub("_spliced", "", gene)#gene name from file name
samp<-name[[1]][1] # Sample name from file name


fout<-paste0(args[2],samp,'_FRMT_',gene, "_translated.fa")  #name of output fasta (protein)
h<-paste0(samp,'_',gene) # just the sample name

#for each blast file
blout<-fas   #grab each file
zz<-pipe(paste0("grep -e \"Identities\" -e \"Query\" -e \"Sbjct\" -e \"Length of query\" ", blout, " | grep -v \"Query=\""))  #create pipe connection object for file
a<-scan(zz, what="", sep="\n") #scan pipe ?
close(zz) #
zz<-pipe(paste0("grep \"letters)\" ", blout)) #new pipe
len<-scan(zz, what="", sep="\n")  #sequence
close(zz)
len<-as.numeric(gsub(",", "",strsplit(strsplit(len, "\\(")[[1]][2], " ")[[1]][1])) #length of sequence
separator<-grep("Identities", a) #

if(length(separator)>1){
    a<-a[(separator[1]+1):(separator[2]-1)]
    b<-a[grep("Query",a)]
    tot<-as.numeric(strsplit(b[length(b)], " ")[[1]][length(strsplit(b[length(b)], " ")[[1]])])
    b<-as.numeric(strsplit(b[1], " ")[[1]][2])
    a<-a[grep("Sbjct",a)]
    a<-gsub("Sbjct: (\\d+)( *+)", "", a, perl=TRUE)
    a<-gsub(" (\\d+)", "", a, perl=TRUE)
    if(b!=1){
        a<-c(paste(collapse="", rep("X", b-1)), a)
		}
    if(tot<len){
        a<-c(a, paste(collapse="", rep("X", len-tot)))
		}
    a<-paste(collapse="", a)
    newseq<-AAStringSet(a)
    names(newseq)<-h
    writeXStringSet(newseq, fout)

}else{#if separator=0
    if(length(a)==1|length(a)==0){ #if no results at all! # seems to be called only for samples that lack AMELY, good!
		a=paste(collapse="", rep("X", 200))
		newseq<-AAStringSet(a)
		names(newseq)<-h
		writeXStringSet(newseq, fout)
        print(paste0("No Results for 1 BLAST ",h))
        
        }else{
			a<-a[(separator[1]+1):(length(a))]
			b<-a[grep("Query",a,ignore.case=TRUE)]
			tot<-as.numeric(strsplit(b[length(b)], " ")[[1]][length(strsplit(b[length(b)], " ")[[1]])])
			b<-as.numeric(strsplit(b[1], " ")[[1]][2])
			a<-a[grep("Sbjct",a)]
			a<-gsub("Sbjct: (\\d+)( *+)", "", a, perl=TRUE)
			a<-gsub(" (\\d+)", "", a, perl=TRUE)
			if(b!=1){
				a<-c(paste(collapse="", rep("X", b-1)), a)
				}
			if(tot<len){
				a<-c(a, paste(collapse="", rep("X", len-tot)))
				}
			a<-paste(collapse="", a)
			newseq<-AAStringSet(a)
			names(newseq)<-h
			writeXStringSet(newseq, fout)
        }        
}
