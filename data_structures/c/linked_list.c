#include <stdio.h>
#include <stdlib.h> // Include stdlib.h for malloc
#include "linked_list.h"

void append_to_list(Node *head, char data){
    if (head->next == NULL)
    {
        head->next = malloc(sizeof(Node));
        head->next->data = data;
        head->next->next = NULL;
    }
    else
    {
        append_to_list(head->next, data);
    }
}

Node *create_new_list(char data){

    Node *head = malloc(sizeof(Node));
    head->data = data;
    head->next = NULL;
    return head;

}

Node *find_item_in_list(Node *head, char item){

    if (head->data == item){
        return head;
    }
    else if (head->next == NULL){
         return NULL;
    }
    return find_item_in_list(head->next, item);

}

char get_item_from_list(Node *head, int index){

    /* A bit of error checking - if the user enters an index less than 0, return -1. Also, if the enter an index that
       is too large, we will hit a null head, in which case we also return a null character to show this.*/
    if (index < 0 || head == NULL){
        return '\0';
    }
    else if (index == 0){
        return head->data;
    }
    return get_item_from_list(head->next, index - 1);

}

int get_list_length(Node *head){

    int length = 0;
    Node *current_node = head;

    while (current_node != NULL){
        length++;
        current_node = current_node->next;
    }

    return length;

}
void print_list(Node *head){

    Node *current_node = head;

    printf("[");

    while (current_node != NULL){
        printf("%c", current_node->data);
        if (current_node->next != NULL){
            printf(", ");
        }
        current_node = current_node->next;
    }

    printf("]\n");

}

void insert_item_into_list(Node *head, char data, int index){

    Node *current = head;
    Node *new = malloc(sizeof(Node));

    for (int i = 0; i < index - 1; i++){
        current = current->next;
    }

    new->data = data;
    new->next = current->next;
    current->next = new;

}

Node *remove_item_from_list(Node *head, int index)
{
    Node *current = head;
    Node *node_to_delete;

    if (index==0){
        Node *new_head = head->next;
        free(head);
        return new_head;
    }

    for (int i = 0; i < index - 1; i++){
        current = current->next;
    }

    node_to_delete = current->next;
    current->next = current->next->next;
    free(node_to_delete);

    return NULL;

}

void delete_list(Node *head)
{
    if (head->next == NULL){
        free(head);
    }
    else{
        delete_list(head->next);
        free(head);
    }

}
