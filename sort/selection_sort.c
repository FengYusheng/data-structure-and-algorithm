#include<stdio.h>

#define MAX 7

int srcArray[7] = {4, 6, 3, 2, 1, 9, 7};

void printArray() {
    int i = 0;
    printf("[");
    for (i = 0; i < MAX; i++) {
        i < MAX - 1 ? printf("%d, ", srcArray[i]) : printf("%d", srcArray[i]);
    }
    printf("]\n");
}

void _swapItem(int *a, int *b) {
    if (a != b) {
        *a = *a ^ *b;
        *b = *a ^ *b;
        *a = *a ^ *b;
    }
}

void selection_sort(int arr[], int len) {
    int i = 0, j = 0, min = 0;

    for (i = 0; i < MAX; i++) {
        printf("Iteration %d#: ", i);
        printArray();
        min = i;
        for (j = i+1; j < MAX; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }

        if (min != i) {
            printf("Items swapped: %d, %d\n", arr[min], arr[i]);
            _swapItem(&arr[min], &arr[i]);
        }

    }
}


int main(void) {
    printf("Input Array: ");
    printArray();
    printf("====================================\n");
    selection_sort(srcArray, MAX);
    printf("Output Array: ");
    printArray();
    printf("====================================\n");
    return 0;
}
