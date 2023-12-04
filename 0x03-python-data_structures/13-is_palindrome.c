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
    int forward, backward = 0, i = 0;

   if (*head == NULL)
    {
        return (1);
    }
    while (current->next != NULL)
    {
        current = current->next;
       backward++;
    }
    current = *head;
     test = malloc(sizeof(int) * backward + 1);
    while (current != NULL)
    {
          
        test[i] = current->n;
        current = current->next; 
        i++; 
    }

    if (i % 2 != 0)
    {
        free(test);
        return (0);
    }

    forward = backward / 2;

    while (i < forward)
    {
        if (test[i] != test[backward])
        return (0);
    }
    free(test);
    return (1);
    


}
