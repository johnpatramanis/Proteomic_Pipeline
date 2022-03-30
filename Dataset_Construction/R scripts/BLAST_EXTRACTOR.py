
from Bio.Blast import NCBIXML

result_handle = open("TEST")

blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)


######## Should be 1 Alignment

SEQ_MAX=0

CHUNKS=[]
for alignment in blast_record.alignments:

    print("****Alignment Number {}****")
    print("sequence:", alignment.title)
    print("length:", alignment.length)
    
    
    for hsp in alignment.hsps:

        CHUNK_HERE=[hsp.sbjct,hsp.query_start,hsp.query_end]
        if hsp.expect<=0.01:
            CHUNKS.append(CHUNK_HERE)
        print(dir(hsp))

        print("e value:", hsp.expect)
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
    print(start,end,len(CHUNK_HERE))
    
    counter=0
    for AA in range(start-1,end):
        if SEQUENCE[AA]=='-':
            SEQUENCE[AA]=CHUNK_HERE[counter]
        else:
            print('Found inconsistency!')
        counter+=1
    
    

print(CHUNKS)
# if SEQUENCE[0]=='-':
    # SEQUENCE=SEQUENCE[1:]

SEQUENCE=''.join(SEQUENCE)
print(SEQUENCE,len(SEQUENCE))