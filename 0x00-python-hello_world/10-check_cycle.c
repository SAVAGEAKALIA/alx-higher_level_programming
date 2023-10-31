#include "lists.h"
/**
  *check_cycle - check if list is in a cycle or not
  *@list: struc/list to check
  *Return: 1 if true and 0 if false
  */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (!list)
	{
		return (0);
	}

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
			return (1);
	}
	return (0);
}
