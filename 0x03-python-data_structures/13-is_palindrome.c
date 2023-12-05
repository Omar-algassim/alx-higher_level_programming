#include "lists.h"
#include <stdlib.h>
/**
 * is_palindeome - test if link list is palindrome or not
 * @head: the head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int *test = NULL;
    int backward = 0, forward = 0, i = 0;

   if (*head == NULL)
    {
        return (1);
    }
    while (current->next != NULL)
    {
		backward++;
		current = current->next;
    }
	backward++;
	if (backward % 2 != 0)
		return (0);
	else
	{
		current = *head;
		test = malloc(sizeof(int) * backward);
		while (current->next != NULL)
		{
			test[forward] = current->n;
			if (forward >= 1)
			{
				
				if(test[i] == current->n)
				{
					printf("iam here\n");
					while (i >= 0)
					{
						printf("comparing : %d and %d and the len is %d\n", test[i], current->n, i);
						if (test[i] != current->n)
						{
							free(test);
							return (0);
						}
					current = current->next;
					i--;
					}
					free(test);
					return (1);
				}
				i++;
			}
			forward++;
			current = current->next;
		}
	}
    free(test);
    return (0);
}
