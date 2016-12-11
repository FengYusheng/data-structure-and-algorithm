#include <stdio.h>
#include <stdbool.h>

#define MAX 6
#define NONE -1

typedef struct _stack {
    int list[MAX];
    int top;
} Stack;

void init(Stack *stack) {
    int i = 0;
    for (i=0; i<MAX; i++) {
        stack->list[i] = NONE;
    }
    stack->top = NONE;
}

void display(Stack *stack) {
    int i = 0;
    printf("Items in stack : ");
    for (i = 0; i < MAX; i++) {
        printf("%d ", stack->list[i]);
    }
    printf("\n");
}

bool isEmpty(Stack *stack) {
    if (NONE == stack->top) {
        return true;
    } else {
        return false;
    }
}

bool isFull(Stack *stack) {
    if (stack->top == MAX - 1) {
        return true;
    } else {
        return false;
    }
}

int peek(Stack *stack) {
    int ret = NONE;
    if (!isEmpty(stack)) {
        ret = stack->list[stack->top];
    } else {
        printf("Stack is empty\n");
    }
    return ret;
}

void push(Stack * const stack, const int item) {
    if (!isFull(stack)) {
        stack->top++;
        stack->list[stack->top] = item;
    } else {
        printf("Stack is full\n");
    }
}

int pop(Stack * const stack) {
    int ret = NONE;
    if (!isEmpty(stack)) {
        ret = stack->list[stack->top];
        stack->top--;
    } else {
        printf("Stack is empty\n");
    }

    return ret;
}

int main(){
    Stack stack;
    bool ret;
    int item, item2;
    init(&stack);
    display(&stack);

    ret = isFull(&stack);
    if (ret) {
        printf("Stack is full\n");
    }

    ret = isEmpty(&stack);
    if (ret) {
        printf("Stack is empty\n");
    }

    for (item = 0; item <= MAX; item++) {
        push(&stack, item);
    }

    item = peek(&stack);
    printf("peek item is %d\n", item);

    for (item = 0; item <= MAX; item++) {
        item2 = pop(&stack);
        if (item2 != NONE) {
            printf("Item %d is popped from stack\n", item2);
        }
    }

    return 0;
}
