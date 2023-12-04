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
    int *test = malloc(sizeof(int) * 3);
    int backward = 0, i = 0;

   if (*head == NULL)
    {
        return (1);
    }
    while (current->next != NULL)
    {
	test = realloc(test, sizeof(int));
	i = current->n;
	test[backward] = i;
	if (test[backward--] == current->n)
	{
		while (backward > 0)
		{
			if (current->n != test[backward])
			{
				free(test);
				return (0);
			}

			backward--;
		}
		free(test);
		return (1);
	}
	current = current->next;
	backward++;
    }
    free(test);
    return (1);
}
