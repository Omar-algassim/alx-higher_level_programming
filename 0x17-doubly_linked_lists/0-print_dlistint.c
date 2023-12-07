#include "lists.h"

/**
 * print_dlistint - print all elemnt in list
 * @h: the header
 * Return: the number of node 
*/

size_t print_dlistint(const dlistint_t *h)
{
    const dlistint_t *current = h;
    int i = 0;

    while (current != NULL)
    {
        printf("%d\n", current->n);
        i++;
        current = current->next;
    }
    return (i);
}