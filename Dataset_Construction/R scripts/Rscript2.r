args = commandArgs(trailingOnly=TRUE)
#command to run:    Rscript Rscript1.r 'sample_file' 'Starts_file' 'EIT_folder_location' 'output_location'
#command to run(from Dataset_Construction folder):    Rscript R\ scripts/Rscript2.r Workspace/GENE_FASTA_FILES/HG00614_FRMT_AMELX.fa starts.txt ./EIT/ Workspace/SPLICED_GENE_FILES/

library(ShortRead)


fas<-args[1]
info<-read.table(args[2], h=T, as.is=T) # name of each gene/ where each gene starts / which strand



#for each fasta file (one fasta per gene)

name<-strsplit(gsub(".fa", "", fas), "/")[[1]][length(strsplit(gsub(".fa", "", fas), "/")[[1]])]
gene<-strsplit(name,"_")[[1]][length(strsplit(name,"_")[[1]])]#gene name from file name
samp<-paste(strsplit(name,"_")[[1]][1:length(strsplit(name,"_")[[1]])-1],collapse='_') # Sample name from file name
fa<-readFasta(fas) #readFasta loads the fasta file into R
fa<-DNAString(as.character(sread(fa))) #Turn iNAString


tab<-read.table(paste0(args[3], gene, "_ei.txt"), as.is=T, sep="\t") # Exon / Intron file

if (nchar(fa)>=700) {
    
    if(info[info[,1]==gene,3]=="+"){ # If the gene of the fasta file is on the (+) strand
        starts<-info[info[,1]==gene,2] #grab first start position
        ends<-NULL
        for(i in 1:length(tab[,1])){   #use intron position to create chunks of introns
            ends<-c(ends, ((starts[length(starts)]+tab[i,2])-1)) # get end position from last start position + length of intron/exon -1
            starts<-c(starts, (starts[length(starts)]+tab[i,2])) # next start position is last end position (+1)
        }
        starts<-starts[1:length(tab[,1])] # remove the last start position
        
        starts<-starts[-grep("Intron", tab[,1])] # remove intron starts from list
        ends<-ends[-grep("Intron", tab[,1])]    #remove intron ends from list
    
    }else{ # if gene of the fasta file is on (-) strand, same as above but the reverse logic (move from right to left)
        ends<-info[info[,1]==gene,2] # what previously would be start is here the end
        starts<-NULL #the same logic as above
        for(i in 1:length(tab[,1])){ #the same logic as in the above loop, but we are moving to the left, so starts are bigger numbers than their ends
            starts<-c(starts, ends[length(ends)]-tab[i,2]+1)
            ends<-c(ends, ends[length(ends)]-tab[i,2])
        }
        
        ends<-ends[1:length(tab[,1])]   #again remove last part
        #remove introns
        starts<-starts[-grep("Intron", tab[,1])]
        ends<-ends[-grep("Intron", tab[,1])]
        starts<-rev(starts) #flip them into canonical order, from smaller number to larger
        ends <-rev(ends)
    }
    
    seqs<-NULL
    #now we use those starts / ends pairs to isolate the exons only from the sequence
    for(i in 1:length(starts)){
        seqs<-paste(sep="", seqs, as.character(fa[starts[i]:ends[i]]))
    }
    seqs<-gsub(" ", "", seqs)
    
    ids<-paste0(samp, "_", gene, "_spliced")
    
    newseq<-ShortRead(sread=DNAStringSet(seqs), id=BStringSet(ids))
    
    writeFasta(newseq, paste0(args[4],samp, "_", gene, "_spliced.fa"))
    
    } else{
    ids<-paste0(samp, "_", gene, "_spliced")
    newseq<-ShortRead(sread=DNAStringSet(as.character(fa)), id=BStringSet(ids))
    writeFasta(newseq, paste0(args[4],samp, "_", gene, "_spliced.fa"))
    }
