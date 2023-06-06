#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the head of the linked list
 * @number: Number to be inserted into the linked list
 *
 * Return: Pointer to the newly inserted node, or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t));
	listint_t *h = *head;

	if (!newNode)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}

	if (number <= h->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	while (h->next)
	{
		if (number <= h->next->n)
		{
			newNode->next = h->next;
			h->next = newNode;
			return (newNode);
		}
		h = h->next;
	}
	h->next = newNode;
	return (newNode);
}
