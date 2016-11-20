#include <stdio.h>

#define MAX 7

int srcArray[MAX] = {4,6,3,2,1,9,7};

void printArray() {
    int i = 0;
    printf("[");
    for (i = 0; i < MAX; i++) {
        i < MAX - 1 ? printf("%d, ", srcArray[i]) : printf("%d", srcArray[i]);
    }
    printf("]\n");
}

void insertion_sort(int arr[], int len) {
    int valueToInsert = 0, hole = 0, i = 0;
    for (hole = 1; hole < len; hole++) {
        printf("iteration %d#: ", hole);
        printArray();
        i = hole;
        valueToInsert = arr[hole];
        while (i > 0 && arr[i-1] > valueToInsert) {
            printf("item moved: %d\n", arr[i-1]);
            arr[i] = arr[i-1];
            i -= 1;
        }
        if (i != hole) {
            printf("item inserted %d at posiston %d\n", valueToInsert, i);
            arr[i] = valueToInsert;
        }
    }
}

int main() {
    printf("Input Array: ");
    printArray();
    printf("=====================================\n");
    insertion_sort(srcArray, MAX);
    printf("Output Array: ");
    printArray();
    printf("======================================\n");
    return 0;
}
