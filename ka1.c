#include<stdio.h>
int main()
{
int n,rs=0,r;
scanf("%d",&n);
while(n!=0)
{
r=n%10;
rs=rs*10 +r;
n/=10;
}
printf("%d",rs);
return 0;
}
