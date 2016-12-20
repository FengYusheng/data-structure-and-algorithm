#include<stdio.h>
#include<stdlib.h>

#define NONE -1

typedef struct _node {
    int data;
    int key;
    int length;
    struct _node * next;
} Node;

Node *head = NULL;

void init(Node **head) {
    if (*head != NULL) {
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
    node->length = 0;
    node->next = NULL;
    *head = node;

    return;
}

void destroy(Node **head) {
    Node *p = *head;
    Node *n = NULL;
    while (p != NULL) {
        n = p->next;
        free(p);
        p = n;
    }
    *head = NULL;
    return;
}

void display(Node const *head) {
    Node *p = NULL;

    if (NULL == head || NULL == head->next) {
        printf("The link is empty.\n");
    } else {
        printf("Original List(length is %d): ", head->length);
        p = head->next;
        while(p != NULL) {
            printf("(%d, %d), ", p->data, p->key);
            p = p->next;
        }
        printf("\n");
    }

    return;
}

void insert_node(Node *head, const int key, const int data, const int pos) {
    Node *p = NULL;

    if (NULL == head) {
        printf("You need to init the head.\n");
        return;
    }

    Node *node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("There is no enough space.\n");
        return;
    }

    node->key = key;
    node->data = data;
    node->length = NONE;
    node->next = NULL;

    p = head;
    while(p->next !=NULL) {
        p = p->next;
        if (pos == p->key) {
            break;
        }
    }

    if (NULL == p->next) {
        p->next = node;
    } else {
        node->next = p->next;
        p->next = node;
    }

    head->length++;
    return;
}

void delete_node(Node * const head, const int key) {
    Node *p = NULL;
    Node *t = NULL;

    if (NULL == head) {
        printf("The link is empty.\n");
        return;
    }

    p = head;
    while (p->next != NULL) {
        if (key == p->next->key) {
            break;
        }
        p = p->next;
    }

    if (NULL == p) {
        printf("The node %d doen't exists in the link.\n", key);
    } else {
        head->length--;
        t = p->next;
        p->next = t->next;
        t->next = NULL;
        free(t);
    }

    return;
}

void sort(Node * const head) {
    Node *current = NULL;
    Node *next_node = NULL;
    int i = 0, valueToInsert=0, temp = 0;

    if (NULL == head || NULL == head->next) {
        printf("The link is empty.\n");
        return;
    }

    current = head->next;
    next_node = current->next;

    while (next_node != NULL) {
        valueToInsert = next_node->data;
        while (current != next_node) {
            if (current->data <= valueToInsert) {
                current = current->next;
                continue;
            }
        }
    }

    return;
}

// Node* search(Node * const head, const int key) {
//
// }

int main() {
    Node *head = NULL;
    init(&head);
    display(head);
    init(&head);
    destroy(&head);
    destroy(&head);

    if (NULL == head) {
        printf("head is NULL\n");
    } else {
        printf("head hasn't been destroied\n");
    }

    init(&head);
    insert_node(head, 1, 1, 1);
    display(head);
    insert_node(head, 3, 3, 3);
    display(head);
    insert_node(head, 2, 2, 1);
    insert_node(head, 4, 4, 1);
    display(head);
    delete_node(head, 4);
    display(head);
    destroy(&head);
    display(head);

    return 0;
}
