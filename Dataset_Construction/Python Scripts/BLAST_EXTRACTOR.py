import sys
from Bio.Blast import NCBIXML

INPUTS=list(sys.argv)
BLAST=INPUTS[1]
print(BLAST)
OUTPUT_DIR=INPUTS[2]

NAME=BLAST.strip().split('.')
NAME='.'.join(NAME[:len(NAME)-1])
NAME=NAME.strip().split('/')
NAME=NAME[len(NAME)-1]


print(NAME)


result_handle = open(BLAST)
blast_records = NCBIXML.parse(result_handle)

try:
    blast_record = next(blast_records)
except:
    blast_record='NULL'



######## Should be 1 Alignment
if blast_record!='NULL':

    SEQ_MAX=0

    CHUNKS=[]
    for alignment in blast_record.alignments:

        print("****Alignment Number {}****")
        print("sequence:", alignment.title)
        print("length:", alignment.length)
        
        
        for hsp in alignment.hsps:
            
            
            print(dir(hsp))
            # for DIR in dir(hsp):
                # print(hsp.DIR)
            
            
            CHUNK_HERE=[hsp.sbjct,hsp.query_start,hsp.query_end]
            PERC_IDENT=(float(hsp.identities)/float(hsp.align_length))
            if ((hsp.expect<=0.00001) and (hsp.bits>=50) and (hsp.score>=50) and (PERC_IDENT>=0.75)) :
                CHUNKS.append(CHUNK_HERE)
            

            print("e value:", hsp.expect)
            print("bit Score:", hsp.bits)
            print("Percentage Identity:", PERC_IDENT)
            print("Length:", hsp.align_length)
            print(hsp.query_start)
            print(hsp.query_end)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
            print('\n')
            
            if hsp.query_end>SEQ_MAX:
                SEQ_MAX=int(hsp.query_end)
            

    SEQUENCE=['-' for x in range(SEQ_MAX)]

    for C in CHUNKS:
        start=int(C[1])
        end=int(C[2])
        
            
            
        CHUNK_HERE=list(C[0])
        print('Found Chunk Matching Protein Template positions: ',start,end,' of length ',len(CHUNK_HERE))
        
        counter=0
        for AA in range(start-1,end):
            if (SEQUENCE[AA]=='-'):
                SEQUENCE[AA]=CHUNK_HERE[counter]
            counter+=1



    SEQUENCE=''.join(SEQUENCE)
    SEQUENCE=SEQUENCE.replace('*','-')
    print('Final Matching Protein: ',SEQUENCE, 'of length: ',len(''.join([x for x in SEQUENCE if x!='X' and x!='-'])))

    


if blast_record=='NULL':
    SEQUENCE=['-' for x in range(100)]
    SEQUENCE=''.join(SEQUENCE)
    print(SEQUENCE)




OUTPUT=OUTPUT_DIR+NAME+'.fa'
OUTPUT=OUTPUT.replace('_spliced.fa', '_translated.fa')
print(OUTPUT)

NAME=NAME.replace('_spliced','')
if NAME.count('-')>=1:
    NAME=NAME.split('-')
    NAME=''.join(NAME[:len(NAME)-1])
    
OUTPUT=open(OUTPUT,'w')
OUTPUT.write('>{}\n'.format(NAME))
OUTPUT.write(SEQUENCE)
OUTPUT.write('\n')
