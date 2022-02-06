#include "holberton.h"

/**
* wildcmp - wild compare function
* @s1: string
* @s2: string to compare
* Return: 1 if match, 0 if not
*/

int wildcmp(char *s1, char *s2)
{
if (*s1 == '\0')
{
if (*s2 == '\0')
return (1);
else if (*s2 == '*')
if (*s2 == '*')
return (wildcmp(s1, s2 + 1));
return (!*s2);
}
if (*s2 == '*')
return (wildcmp(s1 + 1, s2) || wildcmp(s1, s2 + 1));
if (*s1 == *s2)
return (wildcmp(s1 + 1, s2 + 1));
return (0);
}
