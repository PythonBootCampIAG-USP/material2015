#include <stdio.h>
#include <stdlib.h>

double fatC(int N){
   int i;
      int fat=1;
   
   for(i=1;i<=N;i++){
      fat = fat*i;
   }

   return(fat);
}
