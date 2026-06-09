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
        printf("Hello, SendRecv needs >  %d processes\n",size);
    } else if (rank!=0) {
        //Everyone Send to process 0
        message[0]=rank;
        message[1]=size;
        dst=0;
        MPI_Send(message,2,MPI_INT,dst,tag,MPI_COMM_WORLD);
    } else {
        //Process 0 receive from all the others
        for (src=1;src<size;src++) {
            MPI_Recv(message,2,MPI_INT,src,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
            printf("Received mex from rank: %d of %d processes\n",message[0],message[1]);
        }
    }    
    MPI_Finalize();
}