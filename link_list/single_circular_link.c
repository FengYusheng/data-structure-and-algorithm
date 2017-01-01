/*
* Forget the head node.
*/

#include <stdio.h>
#include <stdlib.h>

#define NONE -1

typedef struct _node {
    int key;
    int data;
    int length;
    struct _node *next;
    struct _node *last;
} Node;

Node * init() {
    Node *node = NULL;
    node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("%s: No memory for allocation.\n", __func__);
        return NULL;
    }

    node->key = NONE;
    node->data = NONE;
    node->length = 0;
    node->next = NULL;

    return node;
}

void insert_first(Node* const head, int const key, int const data) {
    Node *node = NULL;

    if (NULL == head) {
        printf("%s: Link is empty, you need to run `init()` firstly.\n", __func__);
        return;
    }

    node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("%s: No memory for allcation.\n", __func__);
        return;
    }

    node->key = key;
    node->data = data;
    node->length = NONE;

    head->length++;
    if (1 == head->length) {
        node->next = node;
        head->last = node;
    } else {
        node->next = head->next;
        head->last->next = node;
    }
    head->next = node;

    return;
}

void insert_last(Node* const head, int const key, int const data) {
    Node *node = NULL;

    if (NULL == head) {
        printf("%s: Link is empty, you need to run `init()` firstly.\n", __func__);
        return;
    }

    node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("%s: No memory for allocation.\n", __func__);
        return;
    }

    node->key = key;
    node->data = data;
    node->length = NONE;

    head->length++;
    if (1 == head->length) {
        node->next = node;
        head->next = node;
    } else {
        node->next = head->next;
        head->last->next = node;
    }
    head->last = node;

    return;
}

void destroy(Node **head) {
    Node *current = NULL;
    Node *p = NULL;

    if (NULL == *head) {
        printf("%s: Link is empty already.\n", __func__);
        return;
    }

    current = (*head)->next;
    (*head)->last->next = NULL;
    while (current != NULL) {
        p = current->next;
        free(current);
        current = p;
    }

    free(*head);
    *head = NULL;

    return;
}

void delete(Node* const head, int const key) {
    Node *t = NULL;
    Node *p = NULL;
    int len = 0;

    if (NULL == head) {
        printf("%s: Link is empty already.\n", __func__);
        return;
    }

    t = head->next;
    p = head;
    len = head->length;
    while (len > 0) {
        if (key == t->key) {
            break;
        }
        p = t;
        t = t->next;
        len--;
    }

    if (!len) {
        printf("%s: Node(%d) isn't at the link.\n", __func__, key);
    } else {
        if (len == head->length) {
            /*first node*/
            head->last->next = t->next;
        } else if (1 == len) {
            /*last node*/
            head->last = p;
        }

        p->next = t->next;
        free(t);
        t = NULL;
        head->length--;
        if (0 == head->length) {
            head->last = NULL;
            head->next = NULL;
        }
    }

    return;
}

void display(Node * const head) {
    Node *current = NULL;

    if (NULL == head) {
        printf("%s: Link is empty.\n", __func__);
        return;
    }

    current = head->next;
    printf("(%d, %d), ", current->key, current->data);
    while (current->next != head->next) {
        current = current->next;
        printf("(%d, %d), ", current->key, current->data);
    }
    printf("\n");

    return;
}

int main() {
    Node *head = NULL;
    head = init();
    insert_first(head, 1, 10);
    insert_first(head, 2, 20);
    insert_first(head, 3, 30);
    display(head);

    insert_last(head, 4, 40);
    insert_last(head, 7, 11);
    display(head);

    delete(head, 3);
    display(head);

    delete(head, 7);
    display(head);

    delete(head, 1);
    display(head);

    destroy(&head);
    display(head);
    return 0;
}
