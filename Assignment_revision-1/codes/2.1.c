#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main(){

    int i,j;
     int N = (int)pow(10,6);
double temp;
FILE *fp;

fp = fopen("gau.dat","w");

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
fclose(fp);
}