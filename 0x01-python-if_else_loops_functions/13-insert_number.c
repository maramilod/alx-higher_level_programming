#include "lists.h"
/**
 * insert_node - function add new node
 * @head: linked list
 * @number: int value
 * Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return NULL;
	new->n = number;
	if (number <= (*head)->n || !(*head))
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	node = *head;
	while (node->next && number > node->next->n)
	{
		node = node->next;
	}
	if (node->next)
		new->next = node->next;
	node->next = new;
	return (new);
}
