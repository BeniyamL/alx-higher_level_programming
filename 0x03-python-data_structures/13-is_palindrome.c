#include "lists.h"
/**
 * is_palindrome - check whether a linked list is a palindrome
 * @head: the head of the linked list
 *
 * Return: 1 if it is palindrome 0 otherwise
 **/
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *end = *head;
	int len = findlength(start), i, total;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	total = len * 2;
	len = total - 2;
	for (i = 0; i < (total / 2); i = i + 2)
	{
		if (start[i].n != end[len].n)
			return (0);
		len = len - 2;
	}
	return (1);
}

/**
 * findlength - find the length of a linked list
 * @h: the head of linked list
 *
 * Return: the length of a list
 **/
int findlength(listint_t *h)
{
	int size = 0;

	while (h)
	{
		size++;
		h = h->next;
	}
	return (size);
}
