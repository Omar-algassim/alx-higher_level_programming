#include "lists.h"
#include <stdlib.h>
/**
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert = malloc(sizeof(listint_t));
	listint_t *temp = *head;
	listint_t *current = *head;

	if(*head == NULL || !number)
		return (NULL);

	insert->n = number;

	while(current->next != NULL)
	{
		if(current->n >= insert->n)
		{
			temp->next = insert;
			insert->next = current;
			return (insert);
		}
	if(current != *head)
		temp = temp->next;	
	current = current->next;
	}
	current->next = insert;
	insert->next = NULL;
	return (insert);
}
