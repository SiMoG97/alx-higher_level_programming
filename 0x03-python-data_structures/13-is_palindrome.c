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
	listint_t *fast = *head, *slow = *head, *revListHead, *h = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast->next && fast->next->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast)
		slow = slow->next;

	revListHead = reverseList(slow);
	while (revListHead)
	{
		if (revListHead->n != h->n)
			return (0);
		revListHead = revListHead->next;
		h = h->next;
	}
	return (1);
}


/**
 * reverseList - a function that reverses a singly linked list
 *
 * @head: the head of the singly linked list
 *
 * Return: a pointer to the head of the reversed list
 */

listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;

	while (head)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}

	return (prev);
}
