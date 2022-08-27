#!/usr/bin/python3
import requests, sys
import re
import sys




def most_common(lst):
    return max(set(lst), key=lst.count)





GENE=sys.argv[1]
ORGANISM=sys.argv[2]




print(GENE,ORGANISM)

ORGANISM_SEARCH='%20'.join(ORGANISM.split('_'))
GENE_ID=''

# requestURL=
requestURL = "https://rest.uniprot.org/uniprotkb/search?query={}&organism={}&format=json".format(GENE,ORGANISM_SEARCH)


r = requests.get(requestURL)

# If any hits
if r.json!=[]:
    MJ=r.json()
    
    
    ### Find best result
    ### If multi-le hits, just get first one
    if (isinstance(MJ, list))==True and (MJ!=[]):
        MJ=MJ[0]
        

    #If single hit, then just select that
    if ((isinstance(MJ, list))==False):
        

        #check if the Gene we are looking for matches the Gene name of the search result OR any of its synonims

        if 'results' in MJ.keys():
            if MJ['results']!=[]:
                MJ=MJ['results'][0]
                if MJ['entryType']=='UniProtKB reviewed (Swiss-Prot)':
                    for DATABASE in MJ['uniProtKBCrossReferences']:
                        if DATABASE['database']=='Ensembl':
                            for PROPER in DATABASE['properties']:
                                if PROPER['key']=='GeneId':
                                    GENE_ID=PROPER['value']

    
    
    
    OUTPUT_FILE=open('Workspace/1_Gene_IDs/{}/{}'.format(ORGANISM,GENE),'w')
    MISSING_IDS=open('Workspace/1_Gene_IDs/{}/Still_Missing_IDs.txt'.format(ORGANISM),'a')
    FOUND_IDS=open('Workspace/1_Gene_IDs/{}/Found_through_Uniprot.txt'.format(ORGANISM),'a')
    
    if GENE_ID!='':
        print(GENE_ID,'\n')
        OUTPUT_FILE.write(str(GENE_ID)+'\n')
        FOUND_IDS.write(str(GENE_ID)+'\n')
    else:
        OUTPUT_FILE.write('NO_ID_FOUND')
        print('NO ID FOUND\n')
        MISSING_IDS.write('{}\n'.format(GENE))



    
        
        