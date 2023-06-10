#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: the singly linked list pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *halfList, *h = *head;
	unsigned int len = 0, halfLen = 0, startAt = 0, i;

	len = linked_list_len(*head);
	if (len == 0)
		return (1);

	halfLen = len / 2;
	startAt = len - halfLen + 1;

	halfList = copy_rev_linked_list(*head, startAt);

	for (i = 1; i <= halfLen; i++)
	{
		if (h->n != halfList->n)
		{
			free_listint(halfList);
			return (0);
		}
		h = h->next;
		halfList = halfList->next;
	}

	free_listint(halfList);
	return (1);
}

/**
 * linked_list_len - Calculates the length of a singly linked list
 *
 * @h: the signly linked list
 *
 * Return: Always 0 (Success)
 */

size_t linked_list_len(listint_t *h)
{
	size_t len = 0;

	while (h)
	{
		h = h->next;
		len++;
	}
	return (len);
}

/**
 * copy_rev_linked_list - Copies a reversed signly linked list
 *			from a given position to a new singly linked list
 *
 * @h: the original signly linked list
 * @startAt: the postion to start copying from
 *
 * Return: a new listint_t
 */

listint_t *copy_rev_linked_list(listint_t *h, unsigned int startAt)
{
	listint_t *current = h;
	listint_t *listCopy = NULL;
	unsigned int i = 1;

	while (current->next)
	{
		if (i < startAt)
		{
			i++;
			current = current->next;
			continue;
		}
		add_nodeint_start(&listCopy, current->n);

		current = current->next;
	}
	add_nodeint_start(&listCopy, current->n);
	return (listCopy);
}

/**
 * add_nodeint_start - adds a new node at the start of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *add_nodeint_start(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

