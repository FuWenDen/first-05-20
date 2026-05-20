#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int fibonacci(int n)
{
    if (n <= 2)
    {
        return 1;
    }
             return  fibonacci(n - 2) + fibonacci(n - 1);
}
int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    int result = fibonacci(n);
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            result = result + i;
        }else
        {
            result = result + n / i;
        }
    }
    printf("Fibonacci number is: %d",result);
    printf("\n");
    return 0;
}