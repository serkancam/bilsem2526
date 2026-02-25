#include <stdio.h>
int say=0;
long long donen=0;
long long fibler[101]={0};
int fib1(int x)
{
    say++;
    
    if(x<=1)
        return 1;
    
    return fib1(x-1)+fib1(x-2);
}
long long int fib2(long long x)
{
    say++;
    
    if(x<=1)
        return 1;
    if(fibler[x]!=0)
        return fibler[x];
    donen=fib2(x-1)+fib2(x-2);
    fibler[x]=donen;
    return donen;
}

int faktoryel(int x)
{
    if(x<=1)
        return 1;
    printf("%d:\n",x);
    return x*faktoryel(x-1);
}

long long int fib3(long long int x)
{
    long long f1=1,f2=1,temp,i;
    if(x<2)
    return 1;
    for(i=2;i<=x;i++)
    {
        temp=f2;
        f2=f1+f2;
        f1=temp;

    }
    say=i;
    return f2;
}
int main()
{
 int a=fib1(21);

 printf("%d-->say=%d\n",a,say++);
  say=0;
  a=fib2(100);

 printf("%lld-->say=%d\n",a,say++);
 say=0;
  a=fib3(100);

 printf("%lld-->say=%d\n",a,say++);
    
}