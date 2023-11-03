#include "hash_tables.h"
/**
 * hash_table_create - function
 * @size: size
 * Return: table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *hash;

	hash = malloc(sizeof(hash_table_t));
	if (!hash)
		return (NULL);
	hash->size = size;
	hash->array = calloc(size, sizeof(hash_node_t));
	if (hash->array == NULL)
	{
		free(hash);
		return (NULL);
	}
	return (hash);
}
