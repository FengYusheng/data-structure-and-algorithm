#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


#define SIZE 5
#define NONE -1


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
} Queue;


static int pos = 0;
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

void enqueue(Queue *const q, const int index)
{
    int rear = q->rear;

    if (isFull(q))
    {
        printf("%s: the queue is full.\n", __func__);
        return;
    }

    rear++;
    rear %= SIZE;
    q->queue[rear] = index;
    q->rear = rear;
    q->count++;
}

int dequeue(Queue *const q)
{
    int front = q->front;
    int ret = NONE;

    if (isEmpty(q))
    {
        printf("%s: queue is empty.\n", __func__);
        return ret;
    }

    front++;
    front %= SIZE;
    ret = q->queue[front];
    q->queue[front] = NONE;
    q->front = front;
    q->count--;

    return ret;
}

void display_queue(Queue *const q)
{
    int i = 0;
    for (i=0; i<SIZE; i++)
    {
        printf("%d ", q->queue[i]);
    }
    printf("\n");
}

void init_edge()
{
    int i = 0, j = 0;

    for (i=0; i<SIZE; i++)
    {
        for (j=0; j<SIZE; j++)
        {
            edges[i][j] = 0;
        }
    }

    return;
}

void add_vertex(const unsigned char label)
{
    Vertex *vertex = NULL;
    if (pos >= SIZE)
    {
        printf("%s: too many vertics.\n", __func__);
        return;
    }

    vertex = (Vertex*)malloc(sizeof(Vertex));
    if (NULL == vertex)
    {
        printf("%s: No memory space to allocate vertex.\n", __func__);
        return;
    }

    vertex->label = label;
    vertex->visited = false;
    vertics[pos++] = vertex;

    return;
}

void add_edge(const int r, const int c)
{
    if (r <= NONE || r >= SIZE)
    {
        printf("%s: r(%d) is invalid.\n", __func__, r);
        return;
    }

    if (c <= NONE || c >= SIZE)
    {
        printf("%s: c(%d) is invalid.\n", __func__, c);
        return;
    }

    edges[r][c] = 1;
    edges[c][r] = 1;

    return;
}

int get_unvisited_adjacent(const int index)
{
    int ret = NONE, i = 0;

    if (index >= SIZE || index <= NONE)
    {
        printf("%s: index(%d) is invalid.\n", __func__, index);
        return ret;
    }

    for (i=0; i<SIZE; i++)
    {
        if (edges[index][i] && false == vertics[i]->visited)
        {
            ret = i;
            break;
        }
    }

    return ret;
}

void display(const int index)
{
    if (index >= SIZE || index <= NONE)
    {
        printf("%s: index(%d) is invalid.\n", __func__, index);
        return;
    }

    printf("%c ", vertics[index]->label);
    vertics[index]->visited = true;

    return;
}

void bft()
{
    Queue queue;
    int i = 0, j = 0;

    init_queue(&queue);

    display(i);
    enqueue(&queue, i);

    while (!isEmpty(&queue))
    {
        i = dequeue(&queue);
        j = get_unvisited_adjacent(i);
        if (j != NONE)
        {
            display(j);
            enqueue(&queue, i);
            enqueue(&queue, j);
        }
    }

    printf("\n");
    return;
}

int main()
{
    add_vertex('S');
    add_vertex('A');
    add_vertex('B');
    add_vertex('C');
    add_vertex('D');
    add_vertex('E');

    init_edge();
    add_edge(0, 1);
    add_edge(0, 2);
    add_edge(0, 3);
    add_edge(1, 4);
    add_edge(2, 4);
    add_edge(3, 4);

    printf("Breadth First Travel: ");
    bft();

    return 0;
}
