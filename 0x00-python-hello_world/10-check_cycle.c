#include "lists.h"
/**
 * check_cycle - check whether a cycle exist in a linked list
 * @list: the head of the linked list
 *
 * Return: 1 if there is a cycle 0 otherwise
 **/
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = list->next->next;
	slow = list->next;
	while(fast && slow && fast->next)
	{
		if (fast == slow)
			return (1);
		fast = fast ->next->next;
		slow = slow->next;
	}
	return (0);
}
