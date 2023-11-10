#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes the node at index of a list.
 * @head: A pointer to a pointer to the head of the doubly linked list.
 * @index: The index of the node to be deleted. Index starts at 0.
 * Return: 1 if it succeeded, -1 if it failed.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current = *head, *temp;
	unsigned int i;

	if (*head == NULL)
	{
        return (-1);
	}

	if (index == 0)
	{	*head = (*head)->next;
		if (*head != NULL)
		{	(*head)->prev = NULL;
		}
		free(current);
		return (1);
    }
	for (i = 0; i < index && current != NULL; i++)
	{	current = current->next;
	}
	if (current == NULL)
	{
        return (-1);
	}
	temp = current->prev;
    temp->next = current->next;

    if (current->next != NULL)
	{	current->next->prev = temp;
	}

    free(current);
    return (1);
}
