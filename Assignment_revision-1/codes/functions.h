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

double mean(FILE *fp){
       double s = 0.0,temp;
  int N = 0;
    while(fscanf(fp,"%lf",&temp)!=EOF)
    { 
        N++;
      s = s + temp;
      
    }
  
    return s/N;
}


double variance(FILE * fp){
    double m = mean(fp),s=0.0,temp;
     fseek(fp, 0, SEEK_SET);
int N=0;
    while(fscanf(fp,"%lf",&temp)!=EOF){
  N++;
  s = s + (temp-m)*(temp - m);

    }
    return s/N;
}

void gaudist(FILE * fp,int N)
{
    double temp; int i,j;
    for (i = 0; i < N; i++)
{
temp = 0;
for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
if(i!=N-1){
fprintf(fp,"%lf\n",temp);
}
else{
    fprintf(fp,"%lf",temp);
}
}
}

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


void tridist(FILE * fp, int N){
    double temp; int i,j;
    for (i = 0; i < N; i++)
{
temp = 0;
for (j = 0; j < 2; j++)
{
temp += (double)rand()/RAND_MAX;
}
if(i!=N-1){
fprintf(fp,"%lf\n",temp);
}
else{
    fprintf(fp,"%lf",temp);
}
}
}