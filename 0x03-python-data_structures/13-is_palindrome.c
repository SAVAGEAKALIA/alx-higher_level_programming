#include "lists.h"
/**
 *is_palindrome- check if the singly list is palindrome
 *@head: head node
 *Return: 1 on failure, 0 on success
 */

int is_palindrome(listint_t **head)
{
	listint_t *bytwo = *head;
	listint_t *byone = *head;
	listint_t *prev  = NULL;
	listint_t *nextnode = NULL;
	int n = 0;

	while (bytwo != NULL && bytwo->next != NULL)
	{	/*bytwo used two move two places so as to reverse only half of list*/
		bytwo = bytwo->next->next;
		byone = byone->next;
		nextnode = byone->next;
		/*prev is = Null making the first node the last node*/
		byone->next = prev;
		/*point prev to address of the first node in the list collecting data*/
		/*collecting data from node list*/
		/*update byone with address of next node in list*/
		prev = byone;
		byone = nextnode;
		n++;
	}

	if (byone != NULL)
	{
		byone = byone->next;
	}

	while (byone != NULL)
	{
		if (byone->n != prev->n)
		{
			return (0);
		}
		byone = byone->next;
		prev = prev->next;
	}
	return (1);
}
