# How to search Gene+Species name --> https://rest.ensembl.org/documentation/info/symbol_lookup
import requests, sys
import re
import time
import json



def most_common(lst):
    return max(set(lst), key=lst.count)



GENE=sys.argv[1]
ORGANISM=sys.argv[2]

OUTPUT_FILE=open('Workspace/1_Gene_IDs/{}/{}'.format(ORGANISM,GENE),'w')
MISSING_IDS=open('Workspace/1_Gene_IDs/{}/Missing_IDs.txt'.format(ORGANISM),'a')

print(GENE,ORGANISM)

server = "https://rest.ensembl.org"
ext = "/lookup/symbol/{}/{}?expand=1".format(ORGANISM,GENE)
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

        
        


if r==[]:
    #if not ok, make sure there is some output/ missing gene folder
    OUTPUT_FILE.write('NO_ID_FOUND')
    print('NO ID FOUND\n')
    MISSING_IDS.write('{}\n'.format(GENE))
    sys.exit()


if r!=[]:
    MJ=r.json()
    
    # print(len(MJ))
    # for L,S in MJ.items():
        # print(L,S)
        # print('\n')
        
    if 'id' in MJ.keys():
        GENE_ID=MJ['id']
        print(GENE_ID,'\n')
        OUTPUT_FILE.write(str(GENE_ID))
        
    else:
        GENE_ID=''
        OUTPUT_FILE.write('NO_ID_FOUND')
        print('NO ID FOUND\n')
        MISSING_IDS.write('{}\n'.format(GENE))
        

   
MISSING_IDS=open('Workspace/1_Gene_IDs/{}/Lost_Connextion_IDs.txt'.format(ORGANISM),'a')
if SERVICE==0:
    MISSING_IDS.write('{}\n'.format(GENE))
    OUTPUT_FILE.write('NO_CONNECTION_TO_SERVER')