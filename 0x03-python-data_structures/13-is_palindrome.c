#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to a pointer to a singly linked list
 *
 * Return: integer, 1 if list is a palindrome else 0
 */
int is_palindrome(listint_t **head)
{
    return palindrome(head, *head);
}

/**
 * palindrome - utility for is_palindrome
 * @left: pointer to a pointer to the left node
 * @right: pointer to the right node
 *
 * Return: integer, 1 if palindrome, else 0
 */
int palindrome(listint_t **left, listint_t *right)
{
    if (right == NULL)
        return 1;

    if (palindrome(left, right->next) && ((*left)->n == right->n))
    {
        *left = (*left)->next;
        return 1;
    }

    return 0;
}
