#include<stdio.h>

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
int main()
{
   FILE * fp;
  fp =  fopen("uni.dat","r");
  double m,v;
  m = mean(fp);
  fseek(fp, 0, SEEK_SET);
  v = variance(fp);
  printf("%lf,  %lf",m,v);
      fclose(fp);
    
}