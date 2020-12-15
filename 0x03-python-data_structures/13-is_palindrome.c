#include "lists.h"
/**
 * reverse_listint - reverses a list
 * @head: the head of the list
 * Return: the head of the reverse
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *p, *tmp;

	if (head == NULL || *head == NULL)
		return (NULL);
	p = NULL;
	while (*head != NULL)
	{
		tmp = (*head)->next;
		(*head)->next = p;
		p = (*head);
		(*head) = tmp;
	}
	(*head) = p;
	return (*head);
}
/**
*listint_len - length of a list
*@h: the head of the list
*Return: number of nodes
*/
size_t listint_len(const listint_t *h)
{
	int i;

	if (h == NULL)
		return (0);
	for (i = 0; h != NULL; i++)
		h = h->next;
	return (i);
}
/**
 * is_palindrome - verify if the list is palindrome
 * @head: head of the list
 * Return: 1 if palindrome 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev;
	size_t len, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	len = listint_len(tmp);
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	return (1);
}
