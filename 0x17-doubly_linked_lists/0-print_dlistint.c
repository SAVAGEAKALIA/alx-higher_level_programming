#include "lists.h"
/**
 *print_dlistint - print element in list
 *@h: head node
 *Return: node number
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current = h;
	size_t n = 0;

	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;

		n++;
	}
	return (n);
}
