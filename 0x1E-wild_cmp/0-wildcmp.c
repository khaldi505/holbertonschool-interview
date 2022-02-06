#include "holberton.h"

/**
* wildcmp - wild compare function
* @s1: a string
* @s2: a string
* Return: 1 if the strings can be considered identical, 0 if not
*/

int wildcmp(char *s1, char *s2)
{
// if *s2 is null, then s1 is null too
if (*s2 == '\0')
return (*s1 == '\0');
// if *s2 is not null, then s1 is not null too
if (*s1 == '\0')
return (*s2 == '*');
// if *s2 is *, then s1 is not null too
if (*s2 == '*')
return (wildcmp(s1 + 1, s2 + 1) || wildcmp(s1 + 1, s2));
// if *s2 is not *, then s1 is not null too
if (*s2 != *s1 && *s2 != '?')
return (0);
return (wildcmp(s1 + 1, s2 + 1));
}
