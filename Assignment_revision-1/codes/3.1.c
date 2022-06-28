#include<stdlib.h>
#include<stdio.h>
#include<math.h>

void randist(FILE * fp,FILE * rfp,int N)
{
    double x;   
    for(int i=0;i<N-1;i++)
    {
        fscanf(rfp,"%lf",&x);
        fprintf(fp,"%lf\n",(-2)*log(1-x));
    }
    fprintf(fp,"%lf",(-2)*log(1-x));
}
int main()
{
    int N = (int)pow(10,6);
    FILE * fp,*rfp; 
    rfp = fopen("uni.dat","r");
    fp = fopen("rand.dat","w");
    randist(fp,rfp,N);
}