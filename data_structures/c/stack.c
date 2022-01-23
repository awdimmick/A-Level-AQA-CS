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

DynamicStack *new_dynamic_stack(void){
    DynamicStack *ds = malloc(sizeof(DynamicStack));
    ds->top = NULL;
    return ds;
}

int dynamic_peek(DynamicStack *s){
    if (s->top != NULL){
        return s->top->data;
    }
    return -1;
};

int dynamic_pop(DynamicStack *s){
    if (s->top == NULL){
        return -1;
    }
    int popped_item = s->top->data;
    Node *popped = s->top;
    s->top = s->top->next;
    free(popped);
    return popped_item;
};

void dynamic_push(int item, DynamicStack *s){
    Node *new = malloc(sizeof(Node));
    new->next = s->top;
    new->data = item;
    s->top = new;
}
bool dyanmic_is_empty(DynamicStack *s){
    return (s->top == NULL);
}