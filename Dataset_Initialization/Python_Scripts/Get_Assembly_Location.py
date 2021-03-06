import requests, sys
import re

#example on how to run: AMELX ENSG00000125363 Homo_sapiens CURRENT



if len(sys.argv)==6:
    GENE=sys.argv[1]
    GENE_ID=sys.argv[2]
    ORGANISM=sys.argv[3]
    ASSEMBLY=sys.argv[4]
    TRANSCRIPT_NAME=sys.argv[5]


elif len(sys.argv)<=5:
    GENE=sys.argv[1]
    GENE_ID=''
    ORGANISM=sys.argv[2]
    ASSEMBLY=sys.argv[3]


START=''
END=''
STRAND=''
SEQ_REGION=''
CURRENT_ASSEMBLY='CURRENT'




server = "http://rest.ensembl.org"
ext = "/lookup/id/{}?expand=1".format(GENE_ID)
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})



# If any hits
if r.json!=[]:
    MJ=r.json()
    
    
    #Find best result!
    #If multiple hits
    if (isinstance(MJ, list))==True: 
        MJ=MJ[0]
    

    if 'error' not in MJ.keys():
        START=MJ['start']
        END=MJ['end']
        IS_CANON=MJ['is_canonical']
        STRAND=MJ['strand']
        SEQ_REGION=MJ['seq_region_name']
        CURRENT_ASSEMBLY=MJ['assembly_name']
        
        print('\nAcquiring Positions of Genes for requested Assembly\n ')
        print('\nCurrent assembly is: {} \n'.format(CURRENT_ASSEMBLY))
        print('Your chosen assembly is: {} \n'.format(ASSEMBLY))
        
        #if user provided with alternative assembly
        if (ASSEMBLY!='CURRENT') and (CURRENT_ASSEMBLY!=ASSEMBLY):
                        
            
            server = "https://rest.ensembl.org"
            ext = "/map/{}/{}/{}:{}..{}:{}/{}?".format(ORGANISM,CURRENT_ASSEMBLY,SEQ_REGION,START,END,STRAND,ASSEMBLY)
             
            r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
            decoded = r.json()
            
            
            #if request gave valid results
            if 'mappings' in decoded.keys():
                NEW_MAP=decoded['mappings'][0]['mapped']
                
                START=NEW_MAP['start']
                END=NEW_MAP['end']
                STRAND=NEW_MAP['strand']
                SEQ_REGION=NEW_MAP['seq_region_name']
                CURRENT_ASSEMBLY=NEW_MAP['assembly']
            else:
                print('Error in finding position of Gene: {} in requested assembly'.format(GENE))
            
print('\nGenerating Gene info for Gene: {}\nLocation: {}:{}-{}\tstrand:{}\nAssembly Name: {}\n Will default to current online assembly if possible.'.format(GENE,SEQ_REGION,START,END,STRAND,CURRENT_ASSEMBLY))             
            

if STRAND==1:
    STRAND='+'
    STARTS_START=1
    
if STRAND==-1:
    STRAND='-'
    STARTS_START=(END-START)
    
else:
    STRAND=='+'
    STARTS_START=1


LOC_FILE=open('Workspace/5_Loc_Files/{}/{}/Gene_locs.txt'.format(ORGANISM,ASSEMBLY),'a')
STARTS_FILE=open('Workspace/5_Loc_Files/{}/{}/starts.txt'.format(ORGANISM,ASSEMBLY),'a')



if ((START!='') and (END!='') and (STRAND!='') and (SEQ_REGION!='') and (GENE_ID!='')):
    #Append the 'Gene_locs.txt' file for that organism/assembly, if Gene info is not missing
    LOC_FILE.write('{}\t{}\t{}\t{}\t{}.fa\n'.format(TRANSCRIPT_NAME,str(SEQ_REGION),str(START),str(END),TRANSCRIPT_NAME))
    if IS_CANON==1:
        LOC_FILE.write('{}\t{}\t{}\t{}\t{}.fa\n'.format(GENE,str(SEQ_REGION),str(START),str(END),GENE))
    
    #Append the 'Starts.txt' file for that organism/assembly
    STARTS_FILE.write('{}\t{}\t{}\n'.format(TRANSCRIPT_NAME,str(STARTS_START),STRAND))
    if IS_CANON==1:
        STARTS_FILE.write('{}\t{}\t{}\n'.format(GENE,str(STARTS_START),STRAND))