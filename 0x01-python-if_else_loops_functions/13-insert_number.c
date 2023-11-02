#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 *insert_node - insert node at a specific position
 *@head: pointer to start of node
 *@number: location to insert new node
 *Return: node on success or Null on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *lastnode = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || number <= (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (lastnode->next != NULL)
	{
		if (lastnode->next->n >= number)
		{
			newnode->next = lastnode->next;
			lastnode->next = newnode;
			return (newnode);
		}
		lastnode = lastnode->next;
	}

	lastnode->next = newnode;

	return (newnode);
}
