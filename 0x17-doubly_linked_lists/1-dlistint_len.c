#include "lists.h"
/**
 *dlistint_len - return number of node
 *@h: head node
 *Return: number of node
 */

size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *current = h;
	size_t n = 0;

	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	return (n);
}
