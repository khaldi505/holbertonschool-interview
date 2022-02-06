#include "holberton.h"

/**
* wildcmp - Compares two string with wild characters
* @s1: a string 
* @s2: s2 can contain the special character *.
* Return:  returns 1 if the strings can be considered identica
*/

int wildcmp(char *s1, char *s2){
int i, j;

i = 0;
j = 0;

while (s1[i] != '\0'){
if (s2[j] == '*'){
j++;
while (s2[j] == '*'){
j++;
}
if (s2[j] == '\0'){
return (1);
}
while (s1[i] != '\0'){
if (wildcmp(s1 + i, s2 + j) == 1){
return (1);
}
i++;
}
return (0);
}
if (s1[i] != s2[j]){
return (0);
}
i++;
j++;
}
if (s2[j] == '\0'){
return (1);
}
while (s2[j] == '*'){
j++;
}
if (s2[j] == '\0'){
return (1);
}
return (0);
}
