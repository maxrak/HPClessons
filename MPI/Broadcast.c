#include <mpi.h>
#include <stdio.h>
#define N 4
int main(int argc, char **argv[]){
    int rank,size;
    int i;
    int A[N];
    int tag=0;
    MPI_Status status;

    MPI_Init(&argc,argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);

    //Inizialize 
    for (i=0;i<N;i++){
        A[i]=0;
    }

    if (size==1) {
        printf("Hello, SendRecv needs >  %d processes\n",size);
        MPI_Finalize();

    } else if (rank==0) {
        //Everyone Send to process 0
        for (i=0;i<N;i++){
            A[i]=i;
        }
    }
    MPI_Bcast(A,N,MPI_INT,0,MPI_COMM_WORLD); 
    printf("bcast from rank: %d of A: %d %d %d %d \n",rank,A[0],A[1],A[2],A[3]);
    MPI_Finalize();
}