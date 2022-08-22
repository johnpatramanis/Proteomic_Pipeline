import requests, sys
import re
import json
import time

#example on how to run: AMELX ENST00000380714 homo_sapiens AMELX-203


if len(sys.argv)==5:
    GENE=sys.argv[1]
    TRNSCR_ID=sys.argv[2]
    ORGANISM=sys.argv[3]
    TRNSCR_NAME=sys.argv[4]


elif len(sys.argv)<=4:
    GENE=sys.argv[1]
    TRNSCR_ID=''
    ORGANISM=sys.argv[2]
    TRNSCR_NAME=''

server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(TRNSCR_ID)
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


EXON_LENGTH_LIST=[]
EXON_NAME_LIST=[]
IS_CANON=0


## If any hits
if r!=[]:
    MJ=r.json()
    
    
    ## Find best result!
    ## If multiple hits
    if (isinstance(MJ, list))==True: 
        MJ=MJ[0]
    

    if 'error' not in MJ.keys():
        start=int(MJ['start'])
        EXON=MJ['Exon']
        IS_CANON=int(MJ['is_canonical'])
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
            



ANY_TRANSCRIPT_FOUND=(TRNSCR_NAME!='')


    


if (IS_CANON==1) or (ANY_TRANSCRIPT_FOUND==0):
    TABLE_FILE_GENE=open('Workspace/4_EITs/{}/{}_ei.txt'.format(ORGANISM,GENE),'w')


if ANY_TRANSCRIPT_FOUND==1:
    TABLE_FILE_TRANSCRIPT=open('Workspace/4_EITs/{}/{}_ei.txt'.format(ORGANISM,TRNSCR_NAME),'w')

    for L in range(0,len(EXON_LENGTH_LIST)):
        TABLE_FILE_TRANSCRIPT.write('{}\t{}\n'.format(EXON_NAME_LIST[L],EXON_LENGTH_LIST[L]))
        if IS_CANON==1:
            TABLE_FILE_GENE.write('{}\t{}\n'.format(EXON_NAME_LIST[L],EXON_LENGTH_LIST[L]))




if (IS_CANON==1) or (ANY_TRANSCRIPT_FOUND==0):    
    TABLE_FILE_GENE.close()
if ANY_TRANSCRIPT_FOUND==1:
    TABLE_FILE_TRANSCRIPT.close()
    
    
    
    
   
MISSING_IDS=open('Workspace/1_Gene_IDs/{}/Lost_Connextion_IDs.txt'.format(ORGANISM),'a')
if SERVICE==0:
    MISSING_IDS.write('{}\n'.format(GENE))