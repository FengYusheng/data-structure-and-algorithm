#include <stdio.h>

#define MAX 10

int fib1(const int length)
{
    int i = 2, f1 = 0, f2 = 1;
    int ret = f1;

    if (length <= 1)
    {
        ret = 0;
    }
    else if (2 == length)
    {
        ret = f1 + f2;
    }
    else
    {
        while (i < length)
        {
            ret = f1 + f2;
            f1 = f2;
            f2 = ret;
            i++;
        }
    }

    return ret;
}

int fib2(const int length)
{
    int ret = 0, f1 = 0, f2 = 1;

    if (length <= 1)
    {
        ret = 0;
    }
    else if (2 == length)
    {
        ret = f1 + f2;
    }
    else
    {
        ret = fib2(length - 1) + fib2(length - 2);
    }

    return ret;
}

int main()
{
    int ret = 0;

    ret = fib1(MAX);
    printf("%d\n", ret);

    ret = fib2(MAX);
    printf("%d\n", ret);

    return 0;
}
