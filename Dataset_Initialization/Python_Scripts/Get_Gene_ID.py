# How to search Gene+Species name --> https://rest.ensembl.org/documentation/info/symbol_lookup
import requests, sys
import re
import time
import json



def most_common(lst):
    return max(set(lst), key=lst.count)



GENE=sys.argv[1]
ORGANISM=sys.argv[2]
GENE_ID=''


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

        


if r!=[]:
    MJ=r.json()
        
    if 'id' in MJ.keys():
        GENE_ID=MJ['id']
        print(GENE_ID,'\n')
        OUTPUT_FILE.write(str(GENE_ID))










##### IF missing, first check for synonims, other codes etc
if ((r==[]) or ('id' not in r.json().keys())) and (GENE_ID==''):
    
    
    ##### Search Xrefs database
    
    server = "https://rest.ensembl.org"
    ext = F"/xrefs/symbol/{ORGANISM}/{GENE}?"
 
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
    
    while ((attempts<10) & (r==[])):
        try:
            r = requests.get(server+ext)
            MJ=r.json()

        except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
            time.sleep(10)
            attempts+=1
            SERVICE=0
            r=[]

        else:
            SERVICE=1
            
    



#### If this found something        
if (((r!=[]) and (SERVICE==1)) and (GENE_ID=='')):
    if (r.headers.get('content-type') == 'application/json'):
        MJ=r.json()
        if MJ!=[]:
        ##### If multiple matches, fetch first one
            if type(MJ) is list:
                MJ=MJ[0]
            
            #### Found an ID
            if 'id' in MJ.keys():
                GENE_ID=MJ['id']
                print(GENE_ID,'\n')
                OUTPUT_FILE.write(str(GENE_ID))
                
            ### if target has not ID  
            if ('id' not in MJ.keys()):
                GENE_ID=''
                OUTPUT_FILE.write('NO_ID_FOUND')
                print('NO ID FOUND\n')
                MISSING_IDS.write('{}\n'.format(GENE))
                
        else:### If empty list is returned
            GENE_ID=''


    



   
    


##### If Gene ID is still missing at the end of the day
if GENE_ID=='':
    OUTPUT_FILE.write('NO_ID_FOUND')
    print('NO ID FOUND\n')
    MISSING_IDS.write('{}\n'.format(GENE))
    
   
##### If gene is missing due to lost connection, add it in a seperate list
LOST_CONNECTION_FILE=open('Workspace/1_Gene_IDs/{}/Lost_Connection.txt'.format(ORGANISM),'a')
if SERVICE==0:
    LOST_CONNECTION_FILE.write('{}\n'.format(GENE))