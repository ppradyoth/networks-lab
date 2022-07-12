#include<stdio.h>
int main()
{
    int a[4],b[4],r[3],s[3],i,q[3];
    printf("\nEnter 4 bit data word");
    for(i=3;i>=0;i--)
    {
        scanf("%d",&a[i]);
    }
    r[0]=(a[2]+a[1]+a[0])%2;
    r[1]=(a[2]+a[0]+a[3])%2;
    r[2]=(a[0]+a[1]+a[3])%2;
    printf("\n7 bit hamming codeword is:\n");
    for(i=3;i>=0;i--)
    {
        printf("%d\t",a[i]);
    }
    for(i=2;i>=0;i--)
    {
        printf("%d\t",r[i]);
    }
    printf("\n");
    printf("\n Enter the 4 bit received word:");
    for (i=3;i>=0;i--)
    {
        scanf("%d",&b[i]);
    }
    s[0]=(b[2]+b[1]+b[0]+r[0])%2;
    s[1]=(b[3]+b[2]+b[1]+r[1])%2;
    s[2]=(b[0]+b[1]+b[3]+r[2])%2;
    printf("\n Syndrome is \n");
    for(i=2;i>=0;i--)
    {
        printf("%d\t",s[i]);
    }
    printf("\n");
    if((s[2]==0)&&(s[1]==0)&&(s[0]==0))
    {
        printf("\nNo error detected");
    }
    if((s[2]==1)&&(s[1]==0&&s[0]==1))
        printf("\nError detected in 1 bit (b0) position from right\n");
    if((s[2]==1)&&(s[1]==1)&&(s[0]==1))
        printf("\nError detected in 2 bit (b1) position from right\n");
    if((s[2]==0)&&(s[1]==1)&&(s[0]==1))
        printf("\nError detected in 3 bit (b2) position from right\n");
    if((s[2]==1)&&(s[1]==1)&&(s[0]==0))
        printf("\nError detected in 4 bit (b3) position from right\n");
    return 1;
}
