#include<stdio.h>
#include<stdlib.h>
int main()
{
 int nf,N,i=1,j=0;
 int no_tr=0;
 printf("Enter the number of frames : \n");
 scanf("%d",&nf);
 printf("Enter the Window Size : \n");
 scanf("%d",&N);
 while(i<=nf)
 {
     int x=0;
     for(j=i;j<i+N && j<=nf;j++)
     {
         printf("Sent Frame %d\n ",j);
         no_tr++;
     }
     for(j=i;j<i+N && j<=nf;j++)
     {
         int flag = rand()%2;
         if(!flag)
             {
                 printf("Acknowledgment for Frame %d\n",j);
                 x++;
             }
         else
             {   printf("Frame %d Not Received\n",j);
                 //nt=j%N;
                 //wf=j-nt;
                 printf("Retransmitting Window");
                 break;
             }
     }
     printf("\n");
     //i+=x;
     i+=x;
 }
 printf("Total number of transmissions : %d",no_tr);
 return 0;
}