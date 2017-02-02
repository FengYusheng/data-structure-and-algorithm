#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _node
{
    int data;
} Node;

#define SIZE 10


Node **create(const int size)
{
    Node **heap = NULL;
    heap = (Node**)malloc(sizeof(Node*) * (size + 1));
    if (NULL == heap)
    {
        printf("%s: No memory for allocation.\n", __func__);
    }

    memset(heap, 0, sizeof(Node*)*(size+1));
    return heap;
}

void destroy(Node *heap[], const int size)
{
    int i = 0;
    for (i=0; i<=size; i++)
    {
        if (heap[i] != NULL)
        {
            free(heap[i]);
            heap[i] = NULL;
        }
    }

    if (heap != NULL)
    {
        free(heap);
        *heap = NULL;
    }
}

int get_parent_index(const int index)
{
    return (index % 2) ? ((index - 1) / 2) : ((index - 2) / 2);
}

int left_child_index(const int index)
{
    return 2 * index + 1;
}

int right_child_index(const int index)
{
    return 2 * index + 2;
}

int get_last_index(Node *heap[], const int size)
{
    int i = 0, ret = size;

    for (i=0; i<size; i++)
    {
        if (NULL == heap[i])
        {
            ret = i;
            break;
        }
    }

    if (size == ret && heap[ret] != NULL)
    {
        free(heap[ret]);
        heap[ret] = NULL;
    }

    return ret;
}

void insert(Node *heap[], const int size, const int data)
{
    int current = 0;
    int parent = 0;
    int index = get_last_index(heap, size);
    Node *temp = NULL;
    Node *node = NULL;
    node = (Node*)malloc(sizeof(Node));
    if (NULL == node)
    {
        printf("%s: No memory for allocation.\n", __func__);
        return;
    }

    node->data = data;
    heap[index] = node;
    current = index;

    while (current)
    {
        parent = get_parent_index(current);
        if (heap[parent]->data < heap[current]->data)
        {
            temp = heap[parent];
            heap[parent] = heap[current];
            heap[current] = temp;
            current = parent;
        }
        else
        {
            break;
        }
    }
}

void remove_root(Node *heap[], const int size)
{
    Node *temp = NULL;
    int current = 0, left = 0, right = 0, i = 0;
    int last = get_last_index(heap, size) - 1;

    if (last <= 0)
    {
        last = 0;
    }

    free(heap[0]);
    heap[0] = NULL;
    heap[0] = heap[last];
    heap[last] = NULL;

    while (current < last)
    {
        left = left_child_index(current);
        right = right_child_index(current);

        if (left >= last)
        {
            break;
        }
        else if (right >= last)
        {
            i = left;
        }
        else
        {
            i = (heap[left]->data > heap[right]->data) ? left : right;
        }

        temp = heap[i];
        heap[i] = heap[current];
        heap[current] = temp;
        current = i;
    }

}

int main()
{
    int i = 0;
    int data[SIZE] = {35, 33, 42, 10, 14, 19, 27, 44, 26, 31};
    Node **heap = create(SIZE);

    for (i=0; i<SIZE; i++)
    {
        insert(heap, SIZE, data[i]);
        printf("heap root is %d\n", heap[0]->data);
    }

    printf("remove root...\n");
    for (i=0; i<SIZE; i++)
    {
        remove_root(heap, SIZE);
        if (heap[0] != NULL)
        {
            printf("heap root is %d\n", heap[0]->data);
        }
    }

    destroy(heap, SIZE);

    return 0;
}
