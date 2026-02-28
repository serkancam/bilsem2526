#include <stdio.h>

int f1(int a);
int f2(int b);
int main()
{
    printf("%d\n",f1(5));
}
int f1(int a)
{
    if(a<2)
    return 1;
    return 3*f1(a-1)+f2(a-1);
}
int f2(int b)
{
    if(b<2)
    return 1;
    return 3*f2(b-1)-1;
}