#include "lists.h"
/**
 *check_cycle - checks if there's a cycle on the linked list.
 *@list: pointer to the head of the list
 *Return: returns 1 if there's a cycle or 0
 */
int check_cycle(listint_t *list)
{
listint_t *slow_checker, *fast_checker;
slow_checker = list;
fast_checker = list;
while (slow_checker != NULL && fast_checker != NULL && fast_checker->next)
{
fast_checker = fast_checker->next->next;
slow_checker = slow_checker->next;
if (slow_checker == fast_checker)
return (1);
}
if (list == NULL)
return (0);
return (0);
}
