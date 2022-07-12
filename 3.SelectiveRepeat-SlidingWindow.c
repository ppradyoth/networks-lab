#include<stdio.h>
#include<time.h>
#include<stdlib.h>
int main()
{
 int w,a,ack,nac,i=1,p;
 printf("Enter the packet size: \n");
 scanf("%d",&a);
 printf("Enter the Window Size : \n");
 scanf("%d",&w);
 while(i<=a)
 {
     printf("Sending packets from %d to %d\n",i,i+w-1);
     for(p=i;p<w+i;p++)
     {
        printf("Transmitting packet %d\n",p);
     }
     nac=i+rand()%w;
     if(nac==i)
     {
        printf("Acknowledgement received for %d\n",nac);
        i=i+w;
        continue;
     }
     printf("No Acknowledgement received for %d\n",nac);
     printf("Sending packet %d\n",nac);
     printf("ACK=%d\n",nac+1);
     printf("ACK=%d\n",i+w);
     i=i+w;
 }
 printf("End of packets so ACK discarded\n");
 return 0;
}