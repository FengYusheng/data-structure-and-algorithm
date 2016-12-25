#include <stdio.h>
#include <stdlib.h>

#define NONE -1

typedef struct _node {
    int data;
    int key;
    int length;
    struct _node *next;
    struct _node *prev;
} Node;

Node * init(Node **last) {
    Node *head = NULL;
    head = (Node*)malloc(sizeof(Node));
    if (NULL == head) {
        printf("No memory space for allocation.\n");
    } else {
        head->data = NONE;
        head->key = NONE;
        head->length = 0;
        head->next = NULL;
        head->prev = NULL;
    }

    *last = head;
    return head;
}

void insert_first(Node * const head, Node **last, int const key, int const data) {
    Node *node = NULL;

    if (NULL == head) {
        printf("%s: The head is NULL.\n", __func__);
        return;
    }

    node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("%s: No memory space for allocation.\n", __func__);
        return;
    }

    node->data = data;
    node->key = key;
    node->next = head->next;
    node->prev = NULL;
    head->next = node;
    head->length++;

    if (1 == head->length) {
        *last = node;
    } else if (head->length > 1) {
        node->next->prev = node;
    }
}

void insert_last(Node **last, Node * const head, int const key, int const data) {
    Node *node = NULL;

    node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("%s: No memory space for allocation.\n", __func__);
        return;
    }

    node->key = key;
    node->data = data;
    node->next = NULL;
    node->prev = NULL;
    if (last != NULL) {
        node->prev = *last;
    }

    *last = node;
    head->length++;
}

void insert_after(Node * const head, Node **last, int key, int data, int after) {
    Node *node = NULL;
    Node *current = NULL;

    if (NULL == head) {
        printf("%s: Link is empty.\n", __func__);
        return;
    }

    node = (Node*)malloc(sizeof(Node));
    if (NULL == node) {
        printf("%s: No memory space for allocation.\n", __func__);
        return;
    }

    node->key = key;
    node->data = data;
    node->next = NULL;
    node->prev = NULL;

    current = head->next;
    while(current != NULL) {
        if (key == current->key) {
            break;
        }
        current = current->next;
    }

    if (NULL == current) {

    } else {

    }

    head->length++;

}

void destroy(Node **head, Node **last) {
    Node *current = NULL;
    Node *t = NULL;

    if (NULL == *head) {
        printf("%s: Link is already empty.\n", __func__);
    } else {
        current = (*head)->next;
        while (current != NULL) {
            t = current->next;
            free(current);
            current = t;
        }
    }

    free(*head);
    *head = NULL;
    *last = NULL;
}

void display_first(Node * const head) {
    Node *current = head;
    if (NULL == current) {
        printf("%s: Link is empty.\n", __func__);
    } else {
        printf("Link is: ");
        while (current->next != NULL) {
            current = current->next;
            printf("(%d, %d),", current->key, current->data);
        }
        printf("\n");
    }
}

void display_last(Node * const last) {
    Node *current = last;
    if (NULL == current) {
        printf("%s: Link is empty.\n", __func__);
    } else {
        printf("Link is (from last): ");
        while (current != NULL) {
            printf("(%d, %d),", current->key, current->data);
            current = current->prev;
        }
        printf("\n");
    }
}

int main() {
    Node *head = NULL;
    Node *last = NULL;

    head = init(&last);
    insert_first(head, &last, 1, 10);
    insert_first(head, &last, 2, 20);
    insert_first(head, &last, 3, 30);
    insert_first(head, &last, 4, 1);
    insert_first(head, &last, 5, 40);
    insert_first(head, &last, 6, 56);

    display_first(head);
    display_last(last);

    insert_last(&last, head, 8, 80);
    display_last(last);

    destroy(&head, &last);
    display_first(head);

    return 0;
}
