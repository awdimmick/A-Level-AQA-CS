//
// Created by Adam Dimmick on 21/11/2021.
//

#include "stack.h"
#include <stdlib.h>

Stack *new_stack(int size){

    Stack *s = malloc(sizeof(Stack));
    s->items = calloc(size, sizeof(int));
    s->maxSize = size;
    s->top = -1;

    return s;
}


int peek(Stack *s){

    if (!stack_empty(s)){
        return s->items[s->top];
    }
    else {
        return -1;
    }
}

int pop (Stack *s){

    if (!stack_empty(s)){
        int item = s->items[s->top];
        s->top--;
        return item;
    }

    return -1;
}

void push (int item, Stack *s){

    if (!stack_full(s)){
        s->top++;
        s->items[s->top] = item;
    }

}
bool stack_empty(Stack *s){
    return s->top == -1;
}
bool stack_full(Stack *s){
    return (s->top == s->maxSize - 1);
}