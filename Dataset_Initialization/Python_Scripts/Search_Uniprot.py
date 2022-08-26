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


# requestURL=
requestURL = "https://rest.uniprot.org/uniprotkb/search?query={}&organism={}&format=json".format(GENE,ORGANISM_SEARCH)


r = requests.get(requestURL)

# If any hits
if r.json!=[]:
    MJ=r.json()
    
    
    ### Find best result
    ### If multi-le hits, just get first one
    GENE_IDs=[]
    if (isinstance(MJ, list))==True and (MJ!=[]):
        MJ=MJ[0]
        

    #If single hit, then just select that
    if (isinstance(MJ, list))==False:
        

        #check if the Gene we are looking for matches the Gene name of the search result OR any of its synonims
        GENE_NAMES=[]
        if 'results' in MJ.keys():
            MJ=MJ['results'][0]
        print(MJ.keys())
        # print(MJ['uniProtKBCrossReferences'])
        print(MJ['entryType'])
        GENE_NAMES.append(MJ['gene'][0]['name']['value'])
        if 'synonyms' in MJ['gene'][0].keys():
            GENE_NAMES.append(MJ['gene'][0]['synonyms'][0]['value'])
        
        
        
        #check if name of match is the same of the organism we are looking for
        MATCH_NAME=re.findall(r"(?=("+'|'.join(GENE_NAMES)+r"))", GENE)
        for L in MJ['organism']['names']:
            if L['type']=='scientific':
                SEARCH_ORGANISM='_'.join(L['value'].split(' ')[0:2])
        MATCH_ORGANISM=( ORGANISM==SEARCH_ORGANISM )



        ## If name of gene can be found among synonims and organism name matches
        if (((MATCH_NAME)!=[]) and (MATCH_ORGANISM)):

        #### then Look up the Enemble gene_ID corresponding to it (if there is one)
            for DATABASE in MJ['dbReferences']:
                if DATABASE['type']=='Ensembl':
                    GENE_IDs.append(DATABASE['properties']['gene ID'])
    
    
    
    
    OUTPUT_FILE=open('Workspace/1_Gene_IDs/{}/{}'.format(ORGANISM,GENE),'w')
    MISSING_IDS=open('Workspace/1_Gene_IDs/{}/Missing_IDs.txt'.format(ORGANISM),'a')
    
    if GENE_IDs!=[]:
        GENE_ID=most_common(GENE_IDs)
        print(GENE_ID,'\n')
        OUTPUT_FILE.write(str(GENE_ID))
    else:
        OUTPUT_FILE.write('NO_ID_FOUND')
        print('NO ID FOUND\n')
        MISSING_IDS.write('{}\n'.format(GENE))



    
        
        