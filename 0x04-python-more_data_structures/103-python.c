#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *bytes_obj)
{
    long int size;
    int i;
    char *trying_str = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(bytes_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(bytes_obj, &trying_str, &size);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", trying_str);
    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", trying_str[i]);
    printf("\n");
}

void print_python_list(PyObject *list_obj)
{
    Py_ssize_t size = 0;
    PyObject *item;
    int i = 0;

    if (PyList_CheckExact(list_obj))
    {
        size = PyList_Size(list_obj);

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)list_obj)->allocated);

        while (i < size)
        {
            item = PyList_GET_ITEM(list_obj, i);
            printf("Element %d: %s\n", i, item->ob_type->tp_name);
            if (PyBytes_Check(item))
                print_python_bytes(item);
            i++;
        }
    }
}
