#include "lists.h"
/**
*insert_node - inserting node in a sorted way
*@head: actual of the list
*@number: content of the new node
*Return: the adress of the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *actual, *new;

	actual = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (actual == NULL || actual->n >= number)
	{
		new->next = actual;
		*actual = *new;
		return (new);
	}
	while (actual && actual->next)
	{
		if (actual->next->n < number)
			actual = actual->next;
		else
		{
			new->next = actual->next;
			actual->next = new;
			break;
		}
	}
	return (new);
}
