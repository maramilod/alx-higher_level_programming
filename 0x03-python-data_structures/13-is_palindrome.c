#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - fun
 * @head: h
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int i, *num, j;
	listint_t *rep;

	if (!head || !(*head))
		return (1);
	rep = *head;
	for (i = 0; rep && rep->next; i++)
		rep = rep->next;
	num = malloc(sizeof(int) * i);
	if (num)
	{
		for (j = 0; j <= i; j++)
		{
			num[j] = (*head)->n;
			*head = (*head)->next;
		}
		for (j = 0; j <= i / 2; j++)
		{
			if (num[j] != num[i - j])
			{
				free(num);
				return (0);
			}
		}
		free(num);
	}
	return (1);
}
