#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <omp.h>

#define N 5
void stampa(int M[N][N]){
    int i,j;
    for (i=0;i<N;i++){
        for (j=0;j<N;j++){
            printf("%d \t",M[i][j]);
        }
        printf("\n");
    }  
    printf("\n");

}
int main() {
    int i,j,k;
    int A[N][N],B[N][N],C[N][N];
    srand(time(NULL));
    for (i=0;i<N;i++){
        for (j=0;j<N;j++){
            A[i][j]= rand()%1000;
            B[i][j]= rand()%1000;
        }
    }
    stampa(A);
    stampa(B);

    for (i=0;i<N;i++){
        for (j=0;j<N;j++){
            C[i][j]=0;
            for (k=0;k<N;k++){
                C[i][j]+= A[i][k]+B[k][j];
            }
        }
    }
    stampa(C);
}