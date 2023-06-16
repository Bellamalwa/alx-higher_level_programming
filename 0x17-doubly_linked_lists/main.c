#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int main(void)
{
    dlistint_t *head = NULL;
    dlistint_t *new_node;
    size_t count;

    /* Create nodes */
    for (int i = 0; i < 5; i++)
    {
        new_node = malloc(sizeof(dlistint_t));
        if (new_node == NULL)
        {
            perror("Error: malloc failed");
            return EXIT_FAILURE;
        }

        new_node->n = i;
        new_node->prev = NULL;
        new_node->next = head;

        if (head != NULL)
            head->prev = new_node;

        head = new_node;
    }

    /* Print list */
    printf("Doubly linked list elements:\n");
    count = print_dlistint(head);
    printf("-> %lu elements\n", count);

    /* Free memory */
    while (head != NULL)
    {
        new_node = head->next;
        free(head);
        head = new_node;
}

return EXIT_SUCCESS;
}
