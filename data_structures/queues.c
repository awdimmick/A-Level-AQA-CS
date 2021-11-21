//
// Queues
// -----
// Example implementations of:
//      - Linear (static) queue
//      - Circular (static) queue
//      - List-based (dynamic) queue
//

#include "queues.h"
#include <stdlib.h>
#include <stdbool.h>

/* Static queue functions */
Queue *new_queue(int capacity){

    Queue *q;
    q = malloc(sizeof(Queue));
    q->fp = q->rp = q->size = 0;
    q->capacity = capacity;
    q->items = calloc(capacity, sizeof(int));
    return q;

}

bool queue_empty(Queue *q){
    return q->size == 0;
}

/* Linear queue functions */
bool linear_queue_full(Queue *q){
    return q->rp == q->capacity;
}

void linear_enqueue(Queue *q, int item){
    if (!linear_queue_full(q)) {
        q->items[q->rp] = item;
        q->size++;
        q->rp++;
    }
}

int linear_dequeue(Queue *q){
    if (!queue_empty(q)){
        int item = q->items[q->fp];
        q->size--;
        q->fp++;
        return item;
    }
    return NULL;
}

/* Circular queue functions */
bool circular_queue_full(Queue *q){
    return q->size == q->capacity;
}

void circular_enqueue(Queue *q, int item){
    if (!circular_queue_full(q)) {
        q->items[q->rp] = item;
        q->size++;
        q->rp = (q->rp + 1) % q->capacity;
    }
}

int circular_dequeue(Queue *q){
    if (!queue_empty(q)){
        int item = q->items[q->fp];
        q->size--;
        q->fp = (q->fp + 1) % q->capacity;
        return item;
    }
    else{
        return NULL;
    }
}

/* List-based queue functions */
ListQueue *new_list_queue(){

    ListQueue *q = malloc(sizeof(ListQueue));
    q->fp = NULL;
    q->rp = NULL;
    return q;
}

bool list_queue_empty(ListQueue *q){
    return (q->fp == NULL);
}

int list_queue_dequeue(ListQueue *q){

    /* if queue is empty, nothing to dequeue, so check that first */
    if (list_queue_empty(q)){
        return NULL;
    }

    int item = q->fp->item;

    /* If there was only 1 item in the queue set rp and fp back to NULL */
    if (q->fp == q->rp){
        q->fp = q->rp = NULL;
    }
    else {
        QueueNode *node_to_free = q->fp;
        q->fp = q->fp->next;
        free(node_to_free);
    }

    return item;

}

void list_queue_enqueue(ListQueue *q, int item){

    /* If queue is empty, need to add new node at start of queue and set fp and rp to point to it */
    if (q->fp == NULL){
        q->fp = q->rp = malloc(sizeof(QueueNode));
        if (q->fp != NULL){
            q->fp->item = item;
        }
    }
    else {
        q->rp->next = malloc(sizeof(QueueNode));
        /* If there is insufficient memory to allocate space for a new node, malloc will return NULL, so
         * test for this before assuming to be able to add data for new item. If there is no space then
         * the code below will not run; the item will simply not be added to the queue. */
        if (q->rp->next != NULL){
            q->rp->next->item = item;
            q->rp->next->next = NULL;
            q->rp = q->rp->next;
        }

    }
}

