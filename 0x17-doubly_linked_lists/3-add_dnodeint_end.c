#include "lists.h"
/**
 *add_dnodeint_end - Adds a new node at the end of a dlistint_t list
 *@head: A pointer to the head of the doubly linked list.
 *@n: The data for the new node.
 *Return: The address of the new element, or NULL if it failed.
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *newnode = malloc(sizeof(dlistint_t));
	dlistint_t *temp = *head;
	int i = 0;

	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = n;
	newnode->prev = NULL;
	newnode->next = NULL;

	if (*head == NULL)
	{
		*head = newnode;
		return (newnode);
	}

	while (temp->next != NULL)
	{
		temp = temp->next;
		i++;
	}

	temp->next = newnode;
	newnode->prev = temp;

	return (newnode);
}
