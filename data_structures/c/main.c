//
// Created by Adam Dimmick on 20/11/2021.
//

#include <stdio.h>
#include "linked_list.h"
#include "queues.h"
#include "stack.h"
#include "graphs.h"

void test_linked_list();
void test_linear_queue();
void test_circular_queue();
void test_list_queue();
void test_stack();
void test_dynamic_stack();

int main(void) {

    //test_linked_list();
    //test_circular_queue();
    //test_list_queue();
    //test_stack();
    //test_linear_queue();
    test_dynamic_stack();
    return 0;
}

void test_dynamic_stack(){

    DynamicStack *ds = new_dynamic_stack();
    printf("Popping items to stack...\n");
    for (int i = 1; i <= 10; i++){
        printf("%d ", i);
        dynamic_push(i, ds);
    }

    printf("\n\nPeeking the top of the stack: %d", dynamic_peek(ds));

    printf("\n\nPopping stack until empty..\n");
    while (!dyanmic_is_empty(ds)){
        printf("%d ", dynamic_pop(ds));
    }
    printf("\n");

}

void test_stack(){

    Stack *s = new_stack(5);

    for (int i = 0; !stack_full(s); i++){
        push(i, s);
    }

    // Output should be 4, 3, 2, 1, 0
    while (!stack_empty(s)){
        printf("%d\n", pop(s));
    }

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