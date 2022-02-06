#include "holberton.h"

// Prototype: int wildcmp(char *s1, char *s2);
// s2 can contain the special character *, which matches any sequence of characters.
// The special char * can replace any string (including an empty string).

int wildcmp(char *s1, char *s2)
{
if (*s2 == '\0')
return (*s1 == '\0');
if (*s1 == '\0')
return (*s2 == '*');
if (*s2 == '*')
return (wildcmp(s1 + 1, s2 + 1) || wildcmp(s1 + 1, s2));
if (*s2 != *s1 && *s2 != '*')
return (0);

if (*s2 == '*')
return (wildcmp(s1 + 1, s2 + 1));


if (*s2 == *s1)
return (wildcmp(s1 + 1, s2 + 1));

return (0);

}