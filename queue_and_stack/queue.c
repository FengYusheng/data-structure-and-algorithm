#include<stdio.h>
#include<stdbool.h>

#define MAX 6
#define NONE -1

typedef struct _queue {
    int array[MAX];
    int front;
    int rear;
} Queue;

void init(Queue *queue) {
    int i = 0;
    queue->front = 0;
    queue->rear = 0;
    for (i = 0; i < MAX; i++) {
        queue->array[i] = NONE;
    }
}

int peek(Queue * const queue) {
    int front = queue->front;
    return queue->array[front];
}

/*How should I confirm whether queue is full?*/
bool isFull(Queue * const queue) {
    int rear = queue->rear;
    if (queue->array[rear] != NONE) {
        return true;
    } else {
        return false;
    }
}

bool isEmpty(Queue * const queue) {
    int front = queue->front;
    int rear = queue->rear;
    if (rear == front && NONE == queue->array[front]) {
        return true;
    } else {
        return false;
    }
}

int enqueue(Queue * const queue, const int item) {
    int ret = -1;
    int rear = queue->rear;
    if (!isFull(queue)) {
        queue->array[rear] = item;
        rear++;
        queue->rear = rear % MAX;
        ret = 0;
    } else {
        printf("The queue is full.\n");
    }
    return ret;
}

int dequeue(Queue * const queue) {
    int ret = -1;
    int front = queue->front;
    if (!isEmpty(queue)) {
        ret = queue->array[front];
        queue->array[front] = NONE;
        front++;
        queue->front = front % MAX;
    } else {
        printf("The queue is empty.\n");
    }
    return ret;
}

int main() {
    int temp = NONE, item = NONE;
    Queue queue;
    init(&queue);
    for (temp = 0; temp <= MAX; temp++) {
        if (enqueue(&queue, temp) == 0) {
            printf("Item %d equeue\n", temp);
        };
    }
    printf("dequeue:\n");
    for (temp = 0; temp <= MAX; temp++) {
        item = dequeue(&queue);
        if (item != -1) {
            printf("Item %d dequeue\n", item);
        }
    }
    return 0;
}
