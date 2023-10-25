#define PY_SSIZE_T_CLEAN
#include "Python.h"


/**
 * print_python_float - fun
 * @p: header
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *list = (PyFloatObject *) p;
	
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == NULL)
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
	else
		printf("  value: %s\n",
				PyOS_double_to_string(list->ob_fval,
					'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_bytes - fun
 * @p: header
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *l = (PyBytesObject *) p;
	long int i, size = l->ob_base.ob_size;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == NULL)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", l->ob_sval);
	size = size < 10 ? size + 1 : 10;
	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %2.2x", l->ob_sval[i] & 0xff);
	putchar('\n');
}



/**
 * print_python_list - fun
 * @p: header
 */
void print_python_list(PyObject *p)
{
	long int i = 0, count = list->ob_base.ob_size;
	const char *type;
	PyListObject *list = (PyListObject *) p;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == NULL)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", count);
	printf("[*] Allocated = %ld\n", list->allocated);
	while (i < count)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (PyBytes_Check((PyObject *) list->ob_item[i]))
			print_python_bytes((PyObject *) list->ob_item[i]);
		else if (PyFloat_Check((PyObject *) list->ob_item[i]))
			print_python_float((PyObject *) list->ob_item[i]);
		i++;
	}
}
