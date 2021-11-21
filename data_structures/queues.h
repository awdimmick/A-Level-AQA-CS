//
// Created by Adam Dimmick on 20/11/2021.
//

#ifndef DATA_STRUCTURES_QUEUES_H
#define DATA_STRUCTURES_QUEUES_H

#include <stdbool.h>

typedef struct queue {
    int size, rp, fp, capacity;
    int *items;
} Queue;

typedef struct queue_list_node{
    int item;
    struct queue_list_node *next;
} QueueNode;

typedef struct list_based_queue {
    /* Notice that there is no need to record size or capacity for a linked-list based queue
     * as it wouldn't make sense to impose that limit. Instead, this dynamic list will continue
     * to grow as needed and will free up space whenever an item is dequeued. */
    QueueNode *fp;
    QueueNode *rp;
} ListQueue;

/* Array-based (fixed capacity) queue function declarations */
Queue *new_queue(int capacity);
bool queue_empty(Queue *q);
/* Linear queue function declarations */
bool linear_queue_full(Queue *q);
void linear_enqueue(Queue *q, int item);
int linear_dequeue(Queue *q);
/* Circular queue function declarations */
bool circular_queue_full(Queue *q);
void circular_enqueue(Queue *q, int item);
int circular_dequeue(Queue *q);
/* List-based queue function declarations */
ListQueue *new_list_queue();
int list_queue_dequeue(ListQueue *q);
void list_queue_enqueue(ListQueue *q, int item);
bool list_queue_empty(ListQueue *q);


#endif //DATA_STRUCTURES_QUEUES_H
