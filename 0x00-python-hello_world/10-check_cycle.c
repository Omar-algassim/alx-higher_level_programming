#include "lists.h"

/**
 * check_cycle - test the linked list if cycle or not
 * @header: the header of linked list
 * Return: 0 if not cycle and 1 if its cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t *current;
	
	if(list != NULL && list->next != NULL)
	{
		ptr = list;
		current = list->next;
	}

	while(current != NULL && current->next != NULL)
	{
		if(ptr == current)
			return (1);
	       current = current->next;	
	}
return (0);
}
