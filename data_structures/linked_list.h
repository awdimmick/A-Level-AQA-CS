//
// Created by Adam Dimmick on 20/11/2021.
//

#ifndef DATA_STRUCTURES_LINKED_LIST_H
#define DATA_STRUCTURES_LINKED_LIST_H

/* Define the list_node data structure */
struct list_node
{
    char data;
    struct list_node *next;
};

/* Rename struct list_node to Node for ease */
typedef struct list_node Node;

/* List function declarations */
void append_to_list(Node *head, char data);
Node *create_new_list(char data);
Node *find_item_in_list(Node *head, char item);
char get_item_from_list(Node *head, int index);
int get_list_length(Node *head);
void print_list(Node *head);
void insert_item_into_list(Node *head, char data, int index);
Node *remove_item_from_list(Node *head, int index);
void delete_list(Node *head);

#endif //DATA_STRUCTURES_LINKED_LIST_H