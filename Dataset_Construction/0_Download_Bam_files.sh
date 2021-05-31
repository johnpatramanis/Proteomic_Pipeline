###Download bam files

# create bam files with regions


mkdir ./BAM_FILES/
cd  BAM_FILES

################### 1KG SAMPLES

# cat ./Inds.txt |while read s_line;
	# do
	# sample=$(echo $s_line |cut -d " " -f 2);
	# pop=$(echo $s_line |cut -f 1 -d " ");
	# link=$(echo $s_line |cut -f 3 -d " ");
	
	# wget -O "$sample".bam  "$link"; ##this part can be adjusted maybe
	
	## correcting labeling of chromosomes so that all are 1,2,3.. instead of chr1,chr2 or chromosome1 etc
	# echo 'Processing Sample '$sample' ';
	# samtools view -H "$sample".bam | sed -e 's/SN:\([0-9XY]\)/SN:chr\1/' -e 's/SN:MT/SN:chrM/' | samtools reheader - "$sample".bam > "$sample"_corrected.bam ;
	
	# samtools index -b "$sample"_corrected.bam ;

	## Isolating each relevant chromosome
	# cut -f 2 ./Gene_locs.txt |sort |uniq |while read chr;
		# do  
			
			# echo 'Isolating Chromosome '$chr' from sample '$sample',  ';
			# samtools view -b "$sample"_corrected.bam chr"$chr" > "$pop"_"$sample"_"$chr".bam ;
			# echo 'Indexing Sample '$pop'_'$sample' ';
			# samtools index -b "$pop"_"$sample"_"$chr".bam;
			
			# sleep 2
			
			
		# done;
		
		
		
	# rm "$sample"_corrected.bam;
	# rm "$sample"_corrected.bam.bai;
	# rm "$sample".bam
		
		
		
		
	# done;




################ SIMONS GENOME DIVERSITY PROJECT


################ ANCIENT SAMPLES   #### need for randomization of heterozygous locs?

#### NEAD SAMPLES
#CHAG
sample="CHAGYR";
pop="NEADERT";
SAMPLE="$sample"_"$pop"_ADNA

cut -f 2 ./Gene_locs.txt |sort |uniq |while read chr;
	do  

	wget -O "$SAMPLE"_"$chr".bam http://ftp.eva.mpg.de/neandertal/Chagyrskaya/bam/chr"$chr"-reali.bam ;
	wget -O "$SAMPLE"_"$chr".bam.bai http://ftp.eva.mpg.de/neandertal/Chagyrskaya/bam/chr"$chr"-reali.bam.bai ;
	
	sleep 2
	
	echo 'Processing Sample '$sample', '$chr' ';
	samtools view -H "$SAMPLE"_"$chr".bam | sed -e 's/SN:\([0-9XY]\)/SN:chr\1/' -e 's/SN:MT/SN:chrM/' | samtools reheader - "$SAMPLE"_"$chr".bam > "$SAMPLE"_"$chr"_corrected.bam ;
	
	samtools index -b "$SAMPLE"_"$chr"_corrected.bam ;
	
	sleep 2
	
	rm "$SAMPLE"_"$chr".bam
	rm "$SAMPLE"_"$chr".bam.bai



done;	
	







#### DENIS
sample="DENISOVA";
pop="DENISOVA";
SAMPLE="$sample"_"$pop"_ADNA

# samtools view -h -b -o "$pop"_"$sample"_"$chr".bam ftp://hgdownload.soe.ucsc.edu/gbdb/hg19/bbi/T_hg19_1000g.bam $chr;

wget ftp://hgdownload.soe.ucsc.edu/gbdb/hg19/bbi/T_hg19_1000g.bam > "$SAMPLE".bam
wget ftp://hgdownload.soe.ucsc.edu/gbdb/hg19/bbi/T_hg19_1000g.bam.bai > "$SAMPLE".bam.bai




#### ANCIENT AMH	

	



cd ..
echo "Finished!";
