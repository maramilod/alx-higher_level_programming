#include "lists.h"
/**
 * check_cycle - function
 * @list: list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	if(!list)
		return(0);
	f = list;
	s = list;

	while (s && s->next && f)
	{
		f = f->next;
		s = s->next->next;
		if (f == s)
			return (1);
	}
	return (0);
}
