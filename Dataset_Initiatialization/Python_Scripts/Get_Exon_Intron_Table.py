import requests, sys
import re

#example on how to run: AMELX ENST00000380714 Homo_sapiens
#example                AMELY ENST00000651267 Homo_sapiens
#                       ENAM ENST00000396073 Homo_sapiens
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


EXON_LENGTH_LIST=[]
EXON_NAME_LIST=[]
# If any hits
if r.json!=[]:
    MJ=r.json()
    
    
    #Find best result!
    #If multiple hits
    if (isinstance(MJ, list))==True: 
        MJ=MJ[0]
    

    if 'error' not in MJ.keys():
        start=int(MJ['start'])
        EXON=MJ['Exon']
        for EX in range(0,len(EXON)):
            
            strand=EXON[EX]['strand']
            start=int(EXON[EX]['start'])
            end=int(EXON[EX]['end'])
                    
            
            EXON_LENGTH_LIST.append((end-start)+1)
            EXON_NAME_LIST.append(EXON[EX]['id'])
            
            if (EX<len(EXON)-1) & (strand==1):
                start_next=int(EXON[EX+1]['start'])-1
                EXON_LENGTH_LIST.append((start_next-end)) #from the end of this exon to the start of the next one lies an intron, get its length
                EXON_NAME_LIST.append('Intron')
            
            if (EX<len(EXON)-1) & (strand==-1):
                end_next=int(EXON[EX+1]['end'])+1 
                EXON_LENGTH_LIST.append((start-end_next)) #same logic as above, but we are in the reverse strand so, each exon is to the left of the previous one
                EXON_NAME_LIST.append('Intron')
            
 
    # for i,k in MJ.items():
        # print(i,k)




#if Transcript ID file empty
if r.json==[]:
    SEQ='-'*100
   
    
TABLE_FILE=open('{}_ei.txt'.format(GENE),'w')

for L in range(0,len(EXON_LENGTH_LIST)):
    TABLE_FILE.write('{}\t{}\n'.format(EXON_NAME_LIST[L],EXON_LENGTH_LIST[L]))
