#include <assert.h>
#include <stdio.h>

#define MAX 20

int srcArray[MAX] = {1,2,3,4,6,7,9,11,12,14,15,16,17,19,33,34,43,45,55,66};

void printArray() {
    int i = 0;
    printf("[");
    for (i=0; i<MAX; i++) {
        i < MAX - 1 ? printf("%d, ", srcArray[i]) : printf("%d", srcArray[i]);
    }
    printf("]\n");
}

int binary_search(int arr[], int len, int value) {
    int low =0, high = 0, mid = 0, position = -1, comparision = 0;
    low = 0;
    high = len - 1;
    if (len <=0) {
        return position;
    }

    while (high >= low) {
        printf("comparision %d#:\n", comparision);
        printf("lower bound is %d\nupper bound is %d\n", low, high);
        mid = low + (high - low) / 2;
        if (value == arr[mid]) {
            position = mid;
            break;
        }
        else if (value > arr[mid]) {
            low = mid;
        }
        else {
            high = mid;
        }

        if (high == low) {
            if (value == arr[low]) {
                position = low;
            }
            break;
        }
        comparision++;
    }

    return position;
}

int main() {
    int position = -1;
    printf("Input Array: ");
    printArray();
    printf("==================================================\n");
    position = binary_search(srcArray, MAX, 55);
    if (position > 0) {
        printf("55 is at position %d\n", position);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
