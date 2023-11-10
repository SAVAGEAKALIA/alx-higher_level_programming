#include "lists.h"
/**
 *add_dnodeint - add node to list
 *@n: data for n
 *@head: head node
 *Return: newnode
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *newnode = malloc(sizeof(dlistint_t));

	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = n;
	newnode->prev = NULL;
	newnode->next = *head;

	if (*head != NULL)
	{
		(*head)->prev = NULL;
	}

	*head = newnode;

	return (newnode);
}
