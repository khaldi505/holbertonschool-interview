#include "lists.h"
/**
* find_listint_loop - Finds the loop in a linked list.
* @head: Pointer to the head of list.
* Return: pointer or null
*/
listint_t *find_listint_loop(listint_t *head)
{
listint_t *nextNode;
listint_t *prev;
nextNode = head;
prev = head;
while (head && nextNode && nextNode->next)
{
head = head->next;
nextNode = nextNode->next->next;
if (head == nextNode)
{
head = prev;
prev =  nextNode;
while (1)
{
nextNode = prev;
while (nextNode->next != head && nextNode->next != prev)
{
nextNode = nextNode->next;
}
if (nextNode->next == head)
break;
head = head->next;
}
return (nextNode->next);
}
}
return (NULL);
}
