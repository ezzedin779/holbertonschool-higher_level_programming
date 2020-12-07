#include "lists.h"
/**
*check_cycle - does this list have a cycle ?
*@list: the list
*Return: 1 if yes 0 if no
*/
int check_cycle(listint_t *list)
{
	listint_t *one, *two;

	if (list == NULL || list->next == NULL)
		return (0);
	one = list->next;
	two = one->next;
	while (one != NULL && two != NULL && two->next != NULL)
	{
		if (one == two)
			return (1);
		one = one->next;
		two = two->next->next;
	}
	return (0);
}
