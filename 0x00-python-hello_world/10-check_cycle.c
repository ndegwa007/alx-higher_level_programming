#include "lists.h"
#include <stdlib.h>


/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to be checked
 *
 * Return: 1 if cycle found or 0 if contrary
 */


int check_cycle(listint_t *list)
{
	listint_t *cat, *mouse;

	if (list == NULL || list->next == NULL)
		return (0);


	cat = list->next;
	mouse = list->next->next;

	while (cat && mouse && mouse->next)
	{
		if (cat == mouse)
		{
			return (1);
		}

		cat = cat->next;
		mouse = mouse->next->next;
	}

	return (0);
}
