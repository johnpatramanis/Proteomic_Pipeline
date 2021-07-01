###Download bam files

cd Workspace/OG_BAM_FILES/

#### DENIS
sample="DENISOVA";
pop="DENISOVA";
SAMPLE="$sample"_"$pop"_ADNA

# samtools view -h -b -o "$pop"_"$sample"_"$chr".bam ftp://hgdownload.soe.ucsc.edu/gbdb/hg19/bbi/T_hg19_1000g.bam $chr;

wget -O "$SAMPLE".bam ftp://hgdownload.soe.ucsc.edu/gbdb/hg19/bbi/T_hg19_1000g.bam
wget -O "$SAMPLE".bam.bai ftp://hgdownload.soe.ucsc.edu/gbdb/hg19/bbi/T_hg19_1000g.bam.bai


sample="HUMAN";
pop="ICELAND";
SAMPLE="$sample"_"$pop"


wget -O "$SAMPLE".bam ftp.sra.ebi.ac.uk/vol1/ERZ324/ERZ324295/LP6005443-DNA_B06.srt.aln.bam


cd  ../../