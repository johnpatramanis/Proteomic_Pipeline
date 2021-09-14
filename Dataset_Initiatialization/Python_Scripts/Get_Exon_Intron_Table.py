import requests, sys
import re

#example on how to run: AMELX ENST00000380714 Homo_sapiens
#Check this: AMELX '' Homo_sapiens or AMELX Homo_sapiens 

if len(sys.argv)==4:
    GENE=sys.argv[1]
    TRNSCR_ID=sys.argv[2]
    ORGANISM=sys.argv[3]


elif len(sys.argv)==3:
    GENE=sys.argv[1]
    TRNSCR_ID=''
    ORGANISM=sys.argv[2]
    SEQ='N'*100


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


#if ID file empty
if r.json==[]:
    SEQ='-'*100
   
    
FASTA='>'+GENE+'_'+ORGANISM+'\n'+SEQ
Fasta_ouptut=open('Workspace/3_FASTA_Seqs/{}/{}.fa'.format(ORGANISM,GENE),'w')
Fasta_ouptut.write(FASTA)
print(FASTA)
