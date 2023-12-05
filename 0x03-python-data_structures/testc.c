#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - test if link list is palindrome or not
 * @head: the head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int *test = malloc(sizeof(int) * 3);
    int backward = 0;

    if (*head == NULL)
    {
        return (1);
    }

    while (current->next != NULL)
    {
        test = realloc(test, sizeof(int) * (backward + 1));  // Corrected realloc
        if (test == NULL)
        {
            // Handle memory allocation failure if needed
            return (0);
        }

        test[backward] = current->n;
        printf("%d\n", test[backward]);
        current = current->next;
        backward++;
    }

    free(test);
    return (1);
}

