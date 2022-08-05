import os
import sys

#### Run file like this :python3 VCF_sample_list_generator.py AltainNead_mq25.vcg.gz:hg19.fa,Chagyrskaya_High_Coverage.vcf.gz:hg19.fa,Denisovan_FULL_mq25.vcf.gz:hg19.fa,LBK_FULL_mq25.vcf.gz:hg19.fa,Mezmeskaya1_FULL_mq25.vcf.gz:hg19.fa,Loschbour_FULL_mq25.vcf.gz:hg19.fa,Ust_Ishim_FULL_mq25.vcf.gz:hg19.fa,Vindija_FULL_mq25.vcf.gz:hg19.fa
#### Requires environment with bcftools activated!


VCF_SAMPLES=open('VCF_Samples.txt','w')

### List of VCF_files. Should be in this format: vcf_filename:Reference_fasta,vcf_filename:Reference_fasta 
### Reference fasta must also exist inside /Dataset_Construction/Reference/
VCF_INPUT=sys.argv[1]
VCF_FILE_LIST={}

VCF_INPUT=VCF_INPUT.strip().split(',')

for J in VCF_INPUT:
    J=J.split(':')
    FILE=J[0]
    REF=J[1]
    VCF_FILE_LIST[FILE]=REF

print(VCF_FILE_LIST)

for VCF,REF in VCF_FILE_LIST.items():
    print(VCF,REF)
    os.system('bcftools query -l {} > TEMP'.format(VCF))

    SMPL_FILE=open('TEMP','r')
    SAMPLES=[]
    for line in SMPL_FILE:
        SAMPLES.append(line.strip())

    for SMPL in SAMPLES:
        VCF_SAMPLES.write('{}\t{}\t{}\n'.format(SMPL,VCF,REF))



os.system('''sed '$d' VCF_Samples.txt;''')

