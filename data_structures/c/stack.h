//
// Created by Adam Dimmick on 21/11/2021.
//

#ifndef DATA_STRUCTURES_STACK_H
#define DATA_STRUCTURES_STACK_H

#include <stdbool.h>

typedef struct stack{

    int *items;
    int maxSize, top;

} Stack;

Stack *new_stack(int size);
int peek(Stack *s);
int pop (Stack *s);
void push (int item, Stack *s);
bool stack_empty(Stack *s);
bool stack_full(Stack *s);

#endif //DATA_STRUCTURES_STACK_H
