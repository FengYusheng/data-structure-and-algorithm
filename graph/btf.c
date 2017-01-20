#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct _vertex
{
    unsigned char label;
    bool visited;
} Vertex;

typedef struct _queue
{
    int front;
    int rear;
    int count;
    int queue[SIZE];
} Queue

#define SIZE 5
#define NONE -1


static Vertex *vertics[SIZE];
static int edges[SIZE][SIZE];

void init_queue(Queue *const q)
{
    int i = 0;

    if (NULL == q)
    {
        printf("%s: q is NULL\n", __func__);
        return;
    }

    q->front = NONE;
    q->rear = NONE;
    q->count = 0;

    for (i=0; i<SIZE; i++)
    {
        q->queue[i] = NONE;
    }

    return;
}

bool isEmpty(Queue *const q)
{
    bool ret = false;

    if (NULL == q)
    {
        printf("%s: q is NULL.\n", __func__);
    }
    else
    {
        ret = (0 == q->count);
    }

    return ret;
}

bool isFull(Queue *const q)
{
    bool ret = false;

    if (NULL == q)
    {
        printf("%s: q is NULL\n", __func__);
    }
    else
    {
        ret = (SIZE == q->count);
    }

    return ret;
}

void enqueue(Queue *const q, const unsigned char label)
{

}

void dequeue(Queue *const q)
{

}

void init_edge()
{
    int i = 0, int j = 0;

    for (i=0; i<SIZE; i++)
    {
        for (j=0; j<SIZE; j++)
        {
            edges[i][j] = 0;
        }
    }

    return;
}

int main()
{
    Queue queue;
    return 0;
}
