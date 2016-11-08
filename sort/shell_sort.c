/*
* Shell sort is a sort of insertion sort.
*/


#include<stdio.h>

#define MAX 7

int intArray[MAX] = {4,6,3,2,1,9,7};

void printArray() {
    int i = 0;
    printf("[");
    for (i = 0; i < MAX; i++) {
        printf("%d", intArray[i]);
        if (i < MAX -1) {
            printf(", ");
        }
    }
    printf("]\n");
}

void shellSort(int arr[], int len) {
    /*calculate the initial interval*/
    int interval = 0;
    while ( interval < len / 3 -1) {
        interval = interval * 3 + 1;
    }

    while (interval > 0) {
        /*insertion sort*/
        int outer = 0, inner = 0, valueToInsert = 0, iteration = 0;
        for (outer = interval, iteration = 0; outer < len; outer++, iteration++) {
            printf("iteration %d#: ", iteration);
            printArray();
            valueToInsert = arr[outer];
            inner = outer;

            /*Insertion sort doen't need swap items.*/
            while (inner > interval - 1 && arr[inner - interval] >= valueToInsert) {
                printf("item moved : %d\n", arr[inner - interval]);
                arr[inner] = arr[inner - interval];
                inner = inner - interval;
            }

            printf("item inserted: %d, at posiston %d\n", valueToInsert, inner);
            arr[inner] = valueToInsert;
        }

        interval = interval / 3 - 1;
    }

}


int main(void) {
    printf("Input array: ");
    printArray();
    printf("===================================\n");
    shellSort(intArray, MAX);
    printf("Output array: ");
    printArray();
    printf("====================================\n");
    return 0;
}
