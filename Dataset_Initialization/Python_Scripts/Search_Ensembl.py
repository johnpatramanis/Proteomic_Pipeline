import requests, sys
import re
#Example input: AMELX ENSG00000125363 Homo_sapiens

def most_common(lst):
    return max(set(lst), key=lst.count)


GENE=sys.argv[1]
GENE_ID=sys.argv[2]
ORGANISM=sys.argv[3]


server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(GENE_ID)
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})


TRNSCRPT_ID=''

# If any hits
if r.json!=[]:
    MJ=r.json()
     
    
    #Check out transcript to find the canonical one
    if (isinstance(MJ, list))==False:
        
        for TRNSCRPT in MJ['Transcript']:
            if TRNSCRPT['is_canonical']==1:
                TRNSCRPT_ID=TRNSCRPT['id']
                break
    
    # Get location info?
    
    
    
    
    
        # for J,K in MJ.items():        
            # print('Label: {} \t Info: {} \n\n'.format(J,K))
    
    
    
    
    
    
    
    OUTPUT_FILE=open('Workspace/2_Transcript_IDs/{}/{}'.format(ORGANISM,GENE),'w')
    
    if TRNSCRPT_ID!='':
        OUTPUT_FILE.write(str(TRNSCRPT_ID))
    else:
        OUTPUT_FILE.write('NO_TRNSCRPT_FOUND')
        MISSING_IDS.write('{}\n'.format(GENE))
    
