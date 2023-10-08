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

	if(!head || !(*head))
		return (1);
	for(i = 0; *head; i++)
		*head = (*head)->next;
	num = malloc(sizeof(int) * i);
	 for(i = 0; *head; i++)
	 {
		 num[i] = (*head)->n;
		 *head = (*head)->next;
	 }
	 i--;
	for(j = 0; i >= j; j++)
		if (num[j] != num[i - j])
		{
			free(num);
			return (0);
		}
	free(num);
	return (1);
}
