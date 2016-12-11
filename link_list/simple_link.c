#include<stdio.h>
#include<stdlib.h>

#define NONE -1

typedef struct _node {
    int data;
    int key;
    struct _node * next;
} Node;

Node *head = NULL;

void init(Node *head) {

    if (head != NULL) {
        printf("Init error: head node isn't empty.\n");
        return;
    }

    Node *node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("Init error: can't alloc memory for head node.\n");
        return;
    }

    node->data = NONE;
    node->key = NONE;
    node->next = NULL;

    return;
}

void destroy(Node *head) {
    if (head != NULL) {
        
    }

    return;
}

void display(Node * const head) {

}

int main() {
    return 0;
}
