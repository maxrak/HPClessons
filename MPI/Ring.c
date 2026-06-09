#include <mpi.h>
#include <stdio.h>

int main(int argc, char **argv[]){
    int rank,size;
    int message[2];
    int dst,src;
    int tag=0;
    MPI_Status status;

    MPI_Init(&argc,argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);

    if (size==1) {
        printf("Hello, Ring needs >  %d processes\n",size);
        MPI_Finalize();

    } else if (rank==0) {
        //Everyone Send to process 0
        message[0]=rank;
        message[1]=size;
        dst=0;
        printf("Start Ring sending to %d\n",rank+1);
        MPI_Send(message,2,MPI_INT,rank+1,tag,MPI_COMM_WORLD);
        MPI_Recv(message,2,MPI_INT,size-1,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
        printf("End Ring receiving from %d\n",size-1);
    } else {
        //Process 0 receive from all the others
        MPI_Recv(message,2,MPI_INT,rank-1,MPI_ANY_TAG,MPI_COMM_WORLD,&status);   
        MPI_Send(message,2,MPI_INT,(rank+1)%size,tag,MPI_COMM_WORLD);
    }    
    MPI_Finalize();
}