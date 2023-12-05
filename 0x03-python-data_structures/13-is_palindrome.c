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
    int *test;
    int backward = 0, forward = 0;

   if (*head == NULL)
    {
        return (1);
    }
    while (current != NULL)
    {
		backward++;
		current = current->next;
    }
	current = *head;
	test = malloc(sizeof(int) * backward);

		while (current != NULL)
		{
			test[forward] = current->n;
			forward++;
			current = current->next;
		}
		current = *head;
		forward = 0;
		while (forward < backward - 1)
		{
			if (test[forward] != test[backward - 1])
			{
				free(test);
				return (0);
			}
			backward--;
			forward++;
		}
    free(test);
    return (1);
}
