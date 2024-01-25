#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object pointer in the project
 * Return: Always nothing
 */

void print_python_bytes(PyObject *p)
{
	char *string_h;
	long int size_p;
	long int j, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size_p = ((PyVarObject *)(p))->ob_size;
	string_h = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size_p);
	printf("  trying string: %s\n", string_h);

	if (size_p >= 10)
		limit = 10;
	else
		limit = size_p + 1;

	printf("  first %ld bytes:", limit);

	for (j = 0; j < limit; j++)
		if (string_h[j] >= 0)
			printf(" %02x", string_h[j]);
		else
			printf(" %02x", 256 + string_h[j]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object pointer in the project
 * Return: always nothing
 */

void print_python_list(PyObject *p)
{
	long int size;
	long int j;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (j = 0; j < size; j++)
	{
		obj = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
