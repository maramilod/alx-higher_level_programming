#include "lists.h"
/**
 * check_cycle - function check a linked list
 * @list: the linked list
 *
 * Return: 0 if the list has no cycle  or 1 if it has
 */
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	if (!list)
		return (0);
	f = list;
	s = list;

	while (list && f->next && f)
	{
		f = f->next;
		s = s->next->next;
		if (f == s)
			return (1);
	}
	return (0);
}
