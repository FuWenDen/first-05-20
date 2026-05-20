#include <stdio.h>
int main()
{
    long long n;
    scanf("%lld",&n);
    while(n > 0)
    {
        printf("%lld", n % 10);
        n = n / 10;
    }
    return 0;
}