#include <mpi.h>
#include <stdio.h>
#define N 40
int main(int argc, char **argv[]){
    int rank,size;
    int i;
    int A[N],local_sum,global_sum;

    MPI_Init(&argc,argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    //Inizialize 
    for (i=0;i<N;i++){
        A[i]=i;
    }

    if (size<4) {
        printf("Hello, need more processes\n");
        MPI_Finalize();
    } 
    //Partial Sum
    local_sum=0;
    for (i=0;i<10;i++){
            local_sum+=A[10*rank+i];
    }
    global_sum=0;
    MPI_Reduce(&local_sum,&global_sum,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD); 
    printf("Reduce rank: %d, local_sum:%d, global_sum: %d\n",rank, local_sum,global_sum);
    if (rank==0) {
        printf("Reduce global_sum: %d\n",global_sum);
    }
    MPI_Finalize();
}