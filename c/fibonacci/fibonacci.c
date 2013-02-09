#include "fibonacci.h"

long fibonacci(int n)
{
    long r;

    if(n <= 1) {
        r = n;
    } else {
        r = fibonacci(n - 1) + fibonacci(n - 2);
    }

    return r;
}
