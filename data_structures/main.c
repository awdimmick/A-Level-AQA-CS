//
// Contains routines for testing each C-based data structure implementation
//

#include <stdio.h>
#include "linked_list.h"
#include "queues.h"

void test_linked_list();
void test_linear_queue();
void test_circular_queue();
void test_list_queue();

int main(void) {

    test_linked_list();
    //test_circular_queue();
    //test_list_queue();

    return 0;
}

void test_list_queue(){

    ListQueue *q = new_list_queue();

    for (int i=0; i<10; i++){
        list_queue_enqueue(q, i);
    }

    for (int i=0; i<5; i++){
        printf("Dequeued %d from front of queue\n", list_queue_dequeue(q));
    }

    printf("Adding new items to the queue...\n");
    for (int i=100; i<110; i++){
        list_queue_enqueue(q, i);
        printf("Enqueing %d\n", i);
    }

    printf("Resuming dequeuing..\n");

    while (!list_queue_empty(q)){
        printf("Dequeued %d from front of queue\n", list_queue_dequeue(q));
    }
}

void test_circular_queue(){

    Queue *q = new_queue(10);

    for (int i = 0; i<5; i++){
        circular_enqueue(q, i);
    }

    while (q->size > 0){
        printf("Item at the front of the queue: %d\n", circular_dequeue(q));
    }

    for (int i = 0; i<10; i++){
        circular_enqueue(q, i);
    }

    while (q->size > 0){
        printf("Item at the front of the queue: %d\n", circular_dequeue(q));
    }
}

void test_linear_queue(){

    Queue *q = new_queue(10);

    for (int i = 0; i<5; i++){
        linear_enqueue(q, i);
    }

    while (q->size > 0){
        printf("Item at the front of the queue: %d\n", linear_dequeue(q));
    }

    for (int i = 0; i<10; i++){
        linear_enqueue(q, i);
    }

    while (q->size > 0){
        printf("Item at the front of the queue: %d\n", linear_dequeue(q));
    }
}

void test_linked_list(){

    // Create the head of the list
    Node *head = create_new_list('A');

    // Add items to the list
    append_to_list(head, 'B');
    append_to_list(head, 'C');
    append_to_list(head, 'D');

    // Test searching for an item in the list:
    char target = 'B';
    printf("'%c' can be found at %p\n", target, find_item_in_list(head, target));

    // Testing getting an item from the list
    printf("The second item is: %c\n", get_item_from_list(head, 1));

    // Testing getting list length
    printf("The length of the list is %d\n", get_list_length(head));

    // Testing printing the list
    print_list(head);

    // Testing inserting at a location
    insert_item_into_list(head, 'N', 2);
    print_list(head);

    // Testing remove item from list at a location
    remove_item_from_list(head, 3);
    print_list(head);

    // Test deleting the list
    delete_list(head);

}
