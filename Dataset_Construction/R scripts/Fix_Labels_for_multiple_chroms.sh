#FIX LABELS

for CHR in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y

do 

	cp  './AltaiNea.hg19_1000g.'$CHR'.dq.bam' './AltaiNea.hg19_1000g_'$CHR'.bam'
	cp  './AltaiNea.hg19_1000g.'$CHR'.dq.bam.bai'  './AltaiNea.hg19_1000g_'$CHR'.bam.bai'
	
done
