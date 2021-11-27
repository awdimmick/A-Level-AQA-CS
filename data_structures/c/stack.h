//
// Created by Adam Dimmick on 21/11/2021.
//

#ifndef DATA_STRUCTURES_STACK_H
#define DATA_STRUCTURES_STACK_H

#include <stdbool.h>
#include "linked_list.h". // available here: https://github.com/awdimmick/A-Level-AQA-CS/tree/master/data_structures/c

typedef struct stack{

    int *items;
    int maxSize, top;

} Stack;

typedef struct dynamicStack{

    Node *top;

} DynamicStack;

DynamicStack *new_dynamic_stack(void);
int dynamic_peek(DynamicStack *s);
int dynamic_pop(DynamicStack *s);
void dynamic_push(int item, DynamicStack *s);
bool dyanmic_is_empty(DynamicStack *s);

Stack *new_stack(int size);
int peek(Stack *s);
int pop (Stack *s);
void push (int item, Stack *s);
bool stack_empty(Stack *s);
bool stack_full(Stack *s);

#endif //DATA_STRUCTURES_STACK_H
