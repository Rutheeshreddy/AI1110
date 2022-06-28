#include<stdlib.h>
#include<stdio.h>
#include<math.h>

void unidist(FILE * fp,int N)
{
    for(int i=0;i<N-1;i++)
    {
        fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
    }
    fprintf(fp,"%lf",(double)rand()/RAND_MAX);
}
int main()
{
    int N = (int)pow(10,6);
    FILE * fp;
    fp = fopen("uni.dat","w");
    unidist(fp,N);
}