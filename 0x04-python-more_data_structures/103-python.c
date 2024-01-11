#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *bytes_obj)
{
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(bytes_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(bytes_obj);
    printf("  size: %ld\n", size);

    char *string_repr = PyBytes_AsString(bytes_obj);
    printf("  trying string: %s\n", string_repr);

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", (unsigned char)string_repr[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *list_obj)
{
    printf("[*] Python list info\n");

    Py_ssize_t size = PyList_Size(list_obj);
    Py_ssize_t allocated = ((PyListObject *)list_obj)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(list_obj, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(element))
        {
            print_python_bytes(element);
        }
        else if (PyFloat_Check(element))
        {
            printf("float\n");
        }
        else if (PyTuple_Check(element))
        {
            printf("tuple\n");
        }
        else if (PyList_Check(element))
        {
            printf("list\n");
        }
        else if (PyLong_Check(element))
        {
            printf("int\n");
        }
        else if (PyUnicode_Check(element))
        {
            printf("str\n");
        }
        else
        {
            printf("[ERROR] Unsupported type\n");
        }
    }
}
