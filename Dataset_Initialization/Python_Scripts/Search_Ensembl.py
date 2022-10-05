import requests, sys
import re
import os
import time
import json
# Example input: AMELX ENSG00000125363 Homo_sapiens ['CANON', 'AHSG-201']
# Another Example: KLK4 ENSG00000167749 homo_sapiens CANON

def most_common(lst):
    return max(set(lst), key=lst.count)


GENE=sys.argv[1]
GENE_ID=sys.argv[2].split('.')[0]
ORGANISM=sys.argv[3]
ISOFORMS=sys.argv[4].split(',')





server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(GENE_ID)
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




TRNSCRPT_IDS=[]

# If any hits
if r!=[]:
    MJ=r.json()
     
    
    ## Check out transcripts to find the desitred isoform(s)
    
    if (isinstance(MJ, list))==False:
        if 'Transcript' in MJ.keys():
            for TRNSCRPT in MJ['Transcript']:
                if ('biotype' in TRNSCRPT.keys()) and ('display_name' in TRNSCRPT.keys()) and ('id' in TRNSCRPT.keys()) and ('is_canonical' in  TRNSCRPT.keys()):
                
                    if ('ALL' in ISOFORMS) and (TRNSCRPT['biotype']=='protein_coding'):
                        TRNSCRPT_IDS.append(TRNSCRPT['id']+'::'+TRNSCRPT['display_name'])
                    
                    
                    else:
                        
                        if ('CANON' in ISOFORMS) and (TRNSCRPT['is_canonical']==1):
                            TRNSCRPT_IDS.append(TRNSCRPT['id']+'::'+TRNSCRPT['display_name'])

                            
                        if (TRNSCRPT['biotype']=='protein_coding') and (TRNSCRPT['display_name'] in ISOFORMS):
                            TRNSCRPT_IDS.append(TRNSCRPT['id']+'::'+TRNSCRPT['display_name'])
    
    
    
        ## Scan Transcript entry info
        # for J,K in MJ.items():        
            # print('Label: {} \t Info: {} \n\n'.format(J,K))
    
    
    
    
    print(TRNSCRPT_IDS)
    OUTPUT_FILE=open('Workspace/2_Transcript_IDs/{}/{}'.format(ORGANISM,GENE),'w')
    MISSING_IDS=open('Workspace/2_Transcript_IDs/{}/Missing_IDs.txt'.format(ORGANISM),'a')

    if TRNSCRPT_IDS==[]:
        MISSING_IDS.write('{}\n'.format(GENE))
    else:

        for TRNSCRPT_ID in TRNSCRPT_IDS:
            OUTPUT_FILE=open('Workspace/2_Transcript_IDs/{}/{}'.format(ORGANISM,GENE),'a')
            if TRNSCRPT_ID!=[]:
                OUTPUT_FILE.write(str(TRNSCRPT_ID)+'\n')


   
LOST_CONNECTION_FILE=open('Workspace/1_Gene_IDs/{}/Lost_Connextion_IDs.txt'.format(ORGANISM),'a')
if SERVICE==0:
    LOST_CONNECTION_FILE.write('{}\n'.format(GENE))
    OUTPUT_FILE.write('NO_CONNECTION_TO_SERVER')