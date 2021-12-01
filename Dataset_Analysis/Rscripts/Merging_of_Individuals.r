library(ShortRead)
library(data.table)
setwd('C:/Users/Johnp/Desktop/Merging_Test/')


fa<-readAAStringSet('CONCATINATED_o.fa')

SK830=fa[which(names(fa)=='SK830')]
SK850=fa[which(names(fa)=='SK850')]
SK14132=fa[which(names(fa)=='SK14132')]
SK_MERGED=c()

for (SITE in 1:length(SK14132[[1]])){
  
  POSITION=c(as.character(SK830[[1]][SITE]),as.character(SK850[[1]][SITE]),as.character(SK14132[[1]][SITE]))
  POSITION=sub("?","",POSITION,fixed=TRUE)
  POSITION=sub("-","",POSITION,fixed=TRUE)
  POSITION=sub("X","",POSITION,fixed=TRUE)
  
  POSITION=unique(POSITION)
  
  if ("" %in% POSITION){
    
    POSITION=POSITION[-(which(POSITION==""))]  #Problem HERE!
    
  }
  
  if (identical(POSITION, character(0))){
    POSITION="?"
    
  }
  if (length(POSITION)>=2){
    print("FOUND DIFFERENCE BETWEEN SAMPLES!")
    print(c(POSITION,SITE))
    
  }
  
  SK_MERGED=c(SK_MERGED,POSITION)
  
}

FA=data.table(as.matrix(fa), keep.rownames = TRUE)
SK_MERGED_2=data.table(matrix(SK_MERGED,nrow=1,ncol=9280))
SK_MERGED_2$rn='SK_MERGED'

FA=rbind(FA,SK_MERGED_2)
FINAL_SEQ<-apply(FA[ ,!"rn"], 1, paste, collapse="")
FINAL_SEQ<-AAStringSet(FINAL_SEQ)
names(FINAL_SEQ)<-FA$rn
writeXStringSet(FINAL_SEQ, "CONCATINATED_MERGED_o.fa")
