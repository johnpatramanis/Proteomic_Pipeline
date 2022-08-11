import requests, sys
import re
import time

#example on how to run: python3  Python_Scripts/Get_Prot_Sequence_Ensembl.py AMELX ENST00000380714 homo_sapiens AMELX-203


if len(sys.argv)==5:
    GENE=sys.argv[1]
    TRNSCR_ID=sys.argv[2]
    ORGANISM=sys.argv[3]
    TRNSCR_NAME=sys.argv[4]

elif len(sys.argv)<5:
    GENE=sys.argv[1]
    TRNSCR_ID=''
    ORGANISM=sys.argv[2]
    SEQ='N'*100
    TRNSCR_NAME=''


server = "http://rest.ensembl.org"
ext = "/sequence/id/{}?type=protein".format(TRNSCR_ID)
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})



# If any hits
if r.json!=[]:
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
        if 'seq' in MJ.keys():
            SEQ=MJ['seq']
            
        else:
            SEQ='X'*100


## If ID file empty
if r.json==[]:
    SEQ='-'*100

   
   
   
######### Check if transcript is canonical

time.sleep(2)
IS_CANON=0
server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(TRNSCR_ID)
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

if r.json!=[]:
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


if (IS_CANON==1) or (ANY_TRANSCRIPT_FOUND==0):
    FASTA_GENE='>'+ORGANISM+'_'+GENE+'\n'+SEQ
    Fasta_ouptut_Gene=open('Workspace/3_FASTA_Seqs/Genes_{}/{}.fa'.format(ORGANISM,GENE),'w')
    Fasta_ouptut_Gene.write(FASTA_GENE)
    print(FASTA_GENE)
    Fasta_ouptut_Gene.close()
    
    
