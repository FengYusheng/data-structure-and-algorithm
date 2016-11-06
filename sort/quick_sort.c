#include<stdio.h>

#define MAX 7
#define ERROR -1

int intArray[MAX] = {4,6,3,2,1,9,7};

void printArray(const int _intArray[], const int len){
    int i = 0;
    printf("Input array: [");
    for (i = 0; i < len; i++) {
        printf("%d ", _intArray[i]);
    }
    printf("]\n");
    printf("==========================\n");
}

void _printArray() {
    int i = 0;
    for (i = 0; i < MAX; i++) {
        printf("%d ", intArray[i]);
    }
    printf("\n");
}

void _swapItem(int *a, int *b) {
    // printf("Item a is %d, Item b is %d\n", a, b);
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
    // printf("Item a is %d, Item b is %d\n", a, b);
}


int partition(int _intArray[], int len) {
    int left = 0, right = len - 1, pivot = right;
    if (right <= 0)
        return ERROR;

    while (left < right) {
        while (left < right && _intArray[left] < _intArray[pivot])
            left++;
        while (left < right && _intArray[right] >= _intArray[pivot])
            right--;

        if (left < right) {
            _swapItem(&_intArray[left], &_intArray[right]);
        }
    }

    // left == right
    printf("pivot swap: %d, %d\n", _intArray[left], _intArray[pivot]);
    _swapItem(&_intArray[left], &_intArray[pivot]);
    pivot = left;
    printf("update array: ");
    _printArray();
    return pivot;
}

void quick_sort(int _intArray[], int len) {
    int pivot = 0;
    if (len <= 1) return;
    pivot = partition(_intArray, MAX);
    partition(_intArray, pivot);
    partition(_intArray+pivot+1, len-pivot-1);
    printf("+++++++++++++++++++++++++++++\n");
}


int main(void) {
    printArray(intArray, MAX);
    quick_sort(intArray, MAX);
    return 0;
}
