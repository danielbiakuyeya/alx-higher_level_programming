#include <stddef.h>
#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: pointer to the starting node of the list to reverse in the project.
 * Return: pointer to the head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head;
	listint_t *previous = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list in the Project.
 * Return: If the linked list is not a palindrome - 0. If the
 * linked list is a palindrome - 1.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *reverse = NULL;
	listint_t *mid = NULL;
	size_t size = 0;
	size_t j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp != NULL)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;

	for (j = 0; j < (size / 2) - 1; j++)
		temp = temp->next;
	if ((size % 2 == 0) && (temp->n != temp->next->n))
		return (0);
	temp = temp->next->next;
	reverse = reverse_listint(&temp);
	mid = reverse;
	temp = *head;

	while (reverse != NULL)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_listint(&mid);
	return (1);
}
