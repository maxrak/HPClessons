#include <mpi.h>
#include <stdio.h>
#define N 4
int main(int argc, char **argv[]){
    int rank,size;
    int i;
    int A[N],B[N];
    int tag=0;
    MPI_Status status;

    MPI_Init(&argc,argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);

    //Inizialize 
    for (i=0;i<N;i++){
        A[i]=0;
        B[i]=0;
    }
    //Each process put its rank in the first element
    A[0]=rank;
    MPI_Gather(A,1,MPI_INT,B,1,MPI_INT,0,MPI_COMM_WORLD); 
    printf("Gather from rank: %d of B: %d %d %d %d \n",rank, B[0],B[1],B[2],B[3]);
    MPI_Finalize();
}