#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
* is_palindrome - checks if the given linked list is palindrome or not
* @head: pointer to the head's first item.
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
int len = 0;
int increment = 0;
int counter = 0;
listint_t *fitem, *litem;
if (!head)
return (0);
if (!(*head))
return (1);


litem = *head;
fitem = *head;
len += 1;


while (litem->next)
{
litem = litem->next;
len++;
}

counter = len / 2;


while (increment <= counter)
{
if (fitem->n != litem->n)
return (0);

fitem += 2;
litem -= 2;
increment++;
}

return (1);
}