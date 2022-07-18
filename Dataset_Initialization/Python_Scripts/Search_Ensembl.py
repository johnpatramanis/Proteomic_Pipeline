import requests, sys
import re
import os
#Example input: AMELX ENSG00000125363 Homo_sapiens ['CANON', 'AHSG-201']

def most_common(lst):
    return max(set(lst), key=lst.count)


GENE=sys.argv[1]
GENE_ID=sys.argv[2]
ORGANISM=sys.argv[3]
ISOFORMS=sys.argv[4].split(',')

print(ISOFORMS)



server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(GENE_ID)
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})


TRNSCRPT_IDS=[]

# If any hits
if r.json!=[]:
    MJ=r.json()
     
    
    ## Check out transcripts to find the desitred isoform(s)
    
    if (isinstance(MJ, list))==False:
        
        for TRNSCRPT in MJ['Transcript']:
            
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


    for TRNSCRPT_ID in TRNSCRPT_IDS:
        

        OUTPUT_FILE=open('Workspace/2_Transcript_IDs/{}/{}'.format(ORGANISM,GENE),'a')
        
        if TRNSCRPT_ID!=[]:
            OUTPUT_FILE.write(str(TRNSCRPT_ID)+'\n')
        else:
            OUTPUT_FILE.write('NO_TRNSCRPT_FOUND')
            MISSING_IDS.write('{}\n'.format(GENE))
    
