#include "lists.h"

/**
 * check_cycle - a function that check if a singly linked list has a cycle
 *
 * @list: a singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slowPtr = list;
	listint_t *fastPtr = list;

	while (fastPtr && fastPtr->next)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;
		if (slowPtr == fastPtr)
			return (1);
	}
	return (0);
}
