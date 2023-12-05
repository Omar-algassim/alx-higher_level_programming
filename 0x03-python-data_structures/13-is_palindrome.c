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
    int backward = 0, forward = 0;

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
		forward = backward / 2;
		current = *head;
		test = malloc(sizeof(int) * backward + 1);
		while (current->next != NULL)
		{
			test[forward] = current->n;
			printf("%d\n", test[forward]);
			if (forward != 0)
			{
				if(test[--forward] == current->n)
				{
					while (forward > 0)
					{
						if (test[forward] != current->n)
						{
							free(test);
							return (0);
						}
					current = current->next;
					forward--;
					}
					free(test);
					return (1);
				}
			}
			current = current->next;
			forward++;
		}
	}
    free(test);
    return (1);
}
