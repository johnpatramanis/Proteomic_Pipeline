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


server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(TRNSCR_ID)
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})



# If any hits
if r.json!=[]:
    MJ=r.json()
    
    
    #Find best result!
    #If multiple hits
    if (isinstance(MJ, list))==True:
        
        LS=MJ[0]
        
        START=int(LS['start'])
        for EXON1,EXON2 in LS['Exon'].items():
            print(EXON1,EXON2)
        
        
        # for i,k in LS.items():
            # print(i,k)
            
        
    
    #If single hit, then just select that
    if (isinstance(MJ, list))==False:
    
        START=int(MJ['start'])
        print(START)
        for EXON1 in MJ['Exon']:
            print(EXON1)
        
        # for i,k in MJ.items():
            # print(i,k)
    





#if Transcript ID file empty
if r.json==[]:
    SEQ='-'*100
   
    
TABLE_FILE=open('{}_ei.txt'.format(GENE),'a')

