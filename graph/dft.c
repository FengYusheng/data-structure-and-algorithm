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

static int stack[SIZE];
static int top = NONE;
static int count = NONE;
static Vertex *vertics[SIZE];
static int edges[SIZE][SIZE];

bool isEmpty()
{
    return NONE == top;
}

bool isFull()
{
    return SIZE == top;
}

int pos()
{
    return top;
}

int pop()
{
    int ret = NONE;

    if (isEmpty())
    {
        printf("%s: stack is empty.\n", __func__);
    }
    else
    {
        ret = stack[top--];
    }

    return ret;
}

void push(int vertex_index)
{
    ++top;

    if (!isFull())
    {
        stack[top] = vertex_index;
    }
    else
    {
        printf("%s: stack is full.\n", __func__);
        --top;
    }
}

int peek()
{
    int ret = NONE;

    if (isEmpty())
    {
        printf("%s: stack is empty.\n", __func__);
    }
    else
    {
        ret = stack[top];
    }

    return ret;
}

void init_edges()
{
    int i = 0, j = 0;

    for (i = 0; i < SIZE; i++)
    {
        for (j = 0; j < SIZE; j++)
        {
            edges[i][j] = 0;
        }
    }

    return;
}

void add_vertex(const unsigned char label)
{
    Vertex *vertex = NULL;

    if (count == SIZE - 1)
    {
        printf("%s: the vertics array is full.\n", __func__);
        return;
    }

    vertex = (Vertex*)malloc(sizeof(Vertex));
    if (NULL == vertex)
    {
        printf("%s: no memory for allocation.\n", __func__);
        return;
    }

    vertex->label = label;
    vertex->visited = false;

    vertics[++count] = vertex;
}

void add_edge(const int r, const int c)
{
    if (r >= SIZE || r <= NONE)
    {
        printf("%s: '%d' is invalid.\n", __func__, r);
        return;
    }

    if (c >= SIZE || c <= NONE)
    {
        printf("%s: '%d' is invalid.\n", __func__, c);
        return;
    }

    edges[r][c] = 1;
    edges[c][r] = 1;

    return;
}

void display_vertex(const int index)
{
    if (index<=NONE || index>=SIZE)
    {
        printf("%s: invalid index.\n", __func__, index);
        return;
    }

    printf("%c ", vertics[index]->label);
}

int get_unvisited_adjacent(const int index)
{
    int i = 0, ret = NONE;

    if (index<=NONE || index>=SIZE)
    {
        printf("%s: invalid index %d.\n", __func__, index);
        return ret;
    }

    for (i=0; i<SIZE; i++)
    {
        if (1==edges[index][i] && false==vertics[i]->visited)
        {
            ret = i;
            break;
        }
    }

    return ret;
}

void dft()
{
    int i = 0, j = 0;

    display_vertex(i);
    vertics[i]->visited = true;
    push(i);

    while(!isEmpty())
    {
        i = pop();
        j = get_unvisited_adjacent(i);
        if (j!=NONE)
        {
            push(i);
            display_vertex(j);
            vertics[j]->visited = true;
            push(j);
        }
    }
    printf("\n");

    for (i=0; i<SIZE; i++)
    {
        vertics[i]->visited = false;
    }

    return;
}

int main()
{
    init_edges();
    add_vertex('S');
    add_vertex('A');
    add_vertex('B');
    add_vertex('C');
    add_vertex('D');

    add_edge(0, 1);
    add_edge(0, 2);
    add_edge(0, 3);
    add_edge(1, 4);
    add_edge(2, 4);
    add_edge(3, 4);

    printf("depth first travel: ");
    dft();

    return 0;
}
