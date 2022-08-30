import requests, sys
import re
import time
import json

#example on how to run: python3  Python_Scripts/Get_Prot_Sequence_Ensembl.py AMELX ENST00000380714 homo_sapiens AMELX-203


if len(sys.argv)>=5:
    GENE=sys.argv[1]
    TRNSCR_ID=sys.argv[2]
    ORGANISM=sys.argv[3]
    TRNSCR_NAME=sys.argv[4]
    ## If transcript ID is found but Ensembl does nto recognize it, Sequence will be -s
    SEQ='-'*100

elif len(sys.argv)<5:
    GENE=sys.argv[1]
    TRNSCR_ID=''
    ORGANISM=sys.argv[2]
    SEQ='N'*100
    TRNSCR_NAME=''


server = "http://rest.ensembl.org"
ext = "/sequence/id/{}?type=protein".format(TRNSCR_ID)
attempts=0
r=[]








while ((attempts<10) & (r==[])):
    try:
        r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
        MJ=r.json()

    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        time.sleep(10)
        attempts+=1
        SERVICE=0
        r=[]

    else:
        SERVICE=1
   




# If any hits
if r!=[]:
    MJ=r.json()
    
    
    #Find best result!
    #If multiple hits
    if (isinstance(MJ, list))==True:
    
        LS=MJ[0]
        
        if 'seq' in LS.keys():
            SEQ=LS['seq']
            
        else:
            SEQ='X'*100
            
        
    
    #If single hit, then just select that
    if (isinstance(MJ, list))==False:
        if 'error' not in MJ.keys():
            if 'seq' in MJ.keys():
                SEQ=MJ['seq']
                
            else:
                SEQ='X'*100



   
   
######### Check if transcript is canonical

time.sleep(2)
IS_CANON=0
server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(TRNSCR_ID)
attempts=0
r=[]


while ((attempts<5) & (r==[])):
    try:
        r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
        MJ=r.json()

    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        time.sleep(10)
        attempts+=1
        SERVICE=0
        r=[]

    else:
        SERVICE=1
 

       
if r!=[]:
    MJ=r.json()
    ## Find best result!
    ## If multiple hits
    if (isinstance(MJ, list))==True: 
        MJ=MJ[0]
    if 'error' not in MJ.keys():
        IS_CANON=int(MJ['is_canonical'])







ANY_TRANSCRIPT_FOUND=(TRNSCR_NAME!='')

if ANY_TRANSCRIPT_FOUND==1:
    FASTA_TRANSCRIPT='>'+ORGANISM+'_'+TRNSCR_NAME+'\n'+SEQ
    Fasta_ouptut_Transcript=open('Workspace/3_FASTA_Seqs/Genes_{}/{}.fa'.format(ORGANISM,TRNSCR_NAME),'w')
    Fasta_ouptut_Transcript.write(FASTA_TRANSCRIPT)
    Fasta_ouptut_Transcript.close()
    print(FASTA_TRANSCRIPT)


if (IS_CANON==1):
    FASTA_GENE='>'+ORGANISM+'_'+GENE+'\n'+SEQ
    Fasta_ouptut_Gene=open('Workspace/3_FASTA_Seqs/Genes_{}/{}.fa'.format(ORGANISM,GENE),'w')
    Fasta_ouptut_Gene.write(FASTA_GENE)
    print(FASTA_GENE)
    Fasta_ouptut_Gene.close()

if (ANY_TRANSCRIPT_FOUND==0) and (TRNSCR_ID!=''):    
    FAILING_ID=open('Workspace/3_FASTA_Seqs//Genes_{}/Failing_IDs.txt'.format(ORGANISM),'a')
    FAILING_ID.write(GENE+'\n')

MISSING_IDS=open('Workspace/1_Gene_IDs/{}/Lost_Connextion_IDs.txt'.format(ORGANISM),'a')
if SERVICE==0:
    MISSING_IDS.write('{}\n'.format(GENE))