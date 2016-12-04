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

int peek(Queue queue) {
    int front = queue.front;
    return queue.array[front];
}

/*How should I confirm whether queue is full?*/
bool isFull(Queue queue) {
    int front = queue.front;
    int rear = queue.rear;
    if (rear == front && queue.array[front] > NONE) {
        return true;
    } else {
        return false;
    }
}

bool isEmpty(Queue queue) {
    int front = queue.front;
    int rear = queue.rear;
    if (front == rear && NONE == queue.array[front]) {
        return true;
    } else {
        return false;
    }
}

int enqueue(Queue queue) {
    int ret = -1;
    int rear = queue.rear;
    if (!isFull(queue)) {
        rear++;
        rear %= MAX;
    }
    return ret;
}

int main() {
    bool a;
    Queue queue;
    init(&queue);
    a = isEmpty(queue);
    printf("%s\n", a?"True":"False");
    return 0;
}
