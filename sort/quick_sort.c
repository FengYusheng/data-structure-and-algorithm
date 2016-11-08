/*
* Devide the array into two smaller arrays.
*/

#include<stdio.h>

#define MAX 7

int intArray[MAX] = {4,6,3,2,1,9,7};


void printArray() {
    int i = 0;
    printf("[");
    for (i = 0; i < MAX; i++) {
        printf("%d ", intArray[i]);
    }
    printf("]\n");
}

void _swapItem(int *a, int *b) {
    /*同一个地址里的值异或，只能是０。*/
    if (a != b) {
        *a = *a ^ *b;
        *b = *a ^ *b;
        *a = *a ^ *b;
    }
}

void quick_sort(int arr[], int len) {
    int left = 0, right = len - 2, pivot = len - 1;

    /*There is only one number.*/
    if (len <= 1) return;

    while (1) {
        while (left < right && arr[left] < arr[pivot])
            left++;
        while (left < right && arr[right] >= arr[pivot])
            right--;

        if (left < right) {
            printf("item swaped: %d, %d\n", arr[left], arr[right]);
            _swapItem(&arr[left], &arr[right]);
        } else {
            break;
        }
    }

    if (arr[left] > arr[pivot]) {
        printf("pivot swaped: %d, %d\n", arr[left], arr[pivot]);
        _swapItem(&arr[left], &arr[pivot]);
        pivot = left;
        printf("update array: ");
        printArray();
    } else {
        /*arr[left] == arr[right] <= arr[pivot]*/
        left++;
        printf("pivot swaped: %d, %d\n", arr[left], arr[pivot]);
        _swapItem(&arr[left], &arr[pivot]);
        pivot = left;
    }

    quick_sort(arr, pivot);
    quick_sort(arr+pivot+1, len-pivot-1);
}


int main(void) {
    printf("Input Array: ");
    printArray();
    printf("===============================\n");
    quick_sort(intArray, MAX);
    printf("Output Array: ");
    printArray();
    printf("================================\n");
    return 0;
}
