#include<stdio.h>
#include<stdbool.h>

#define MAX 10

int srcArray[MAX] = {1,8,4,6,0,3,5,2,7,9};

void printArray() {
    int i = 0;
    printf("[");
    for (i = 0; i < MAX; i++) {
        i < MAX - 1 ? printf("%d, ", srcArray[i]) : printf("%d", srcArray[i]);
    }
    printf("]\n");
}

void _swapItems(int *a, int *b) {
    if (a != b) {
        *a = *a ^ *b;
        *b = *a ^ *b;
        *a = *a ^ *b;
    }
}

void bubble_sort(int arr[], int len) {
    int i = 0, j = 0;
    bool swapped = false;
    for (i = 0; i < len - 1; i++) {
        printf("iteration %d#: ", i);
        printArray();
        for (j = 0; j < len - i - 1; j++) {
            printf("Items compared: %d %d", arr[j], arr[j+1]);
            if (arr[j] > arr[j+1]) {
                _swapItems(&arr[j], &arr[j+1]);
                swapped = true;
                printf("                           ==> swapped [%d %d]\n", arr[j], arr[j+1]);
            } else {
                printf("                           ==> not swapped\n");
            }
        }
        if (false == swapped) {
            break;
        }
    }
}

int main() {
    printf("Input array: ");
    printArray();
    bubble_sort(srcArray, MAX);
    printf("Output array: ");
    printArray();
    return 0;
}
