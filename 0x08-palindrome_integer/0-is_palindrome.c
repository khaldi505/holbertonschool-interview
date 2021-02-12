#include "palindrome.h"
#include <stdio.h>
/**
*is_palindrome: checks if the given int is a palindrome
*@n: int
*Return: 1 if yes, 0 if not
**/

int is_palindrome(unsigned long n){
unsigned long int r;
unsigned long i;
r = 0;
i = n;
while (i != 0)
{
r = r * 10;
r = r + i%10;
i = i/10;
}

if (r == n)
{
    return (1);
}
return (0);
}
