#include<stdio.h>
#include<string.h>

int srcArray[10] = {10, 14, 19, 26, 27, 31, 33, 35, 42, 44};
int dstArray[10] = {0};

void printArray(int arr[], int len) {
    int i = 0;
    printf("[");
    for (i = 0; i < len; i++) {
        i == (len - 1) ? printf("%d", arr[i]) : printf("%d, ", arr[i]);
    }
    printf("]\n");
}

static void _merge(const int arr1[], const int arr1_len, \
                   const int arr2[], const int arr2_len, \
                   int dst[]) {

    int i = 0, j = 0, p = 0;
    while (i < arr1_len && j < arr2_len) {
        if (arr1[i] <= arr2[j]) {
            dst[p++] = arr1[i++];
        } else {
            dst[p++] = arr2[j++];
        }
    }

    if (i < arr1_len) {
        while (i < arr1_len)
            dst[p++] = arr1[i++];
    } else if (j < arr2_len) {
        while (j < arr2_len)
            dst[p++] = arr2[j++];
    }
}

void merge_sort(const int src[], int dst[], int len) {
    if (len <= 1) {
        return;
    }

    int mid = len / 2;
    int len1 = mid, len2 = len - mid;
    int i = 0, j = 0;
    int list1[len1], dst1[len1];
    int list2[len2], dst2[len2];

    /*divide the source sort*/
    for (i = 0; i < mid; i++) list1[i] = src[i];
    for (i = mid, j = 0; i < len; i++, j++) list2[j] = src[i];

    merge_sort(list1, dst1, len1);
    merge_sort(list2, dst2, len2);

    _merge(list1, len1, list2, len2, dst);

    return;
}


int main(void) {
    printf("List before sorting: ");
    printArray(srcArray, 10);
    merge_sort(srcArray, dstArray, 10);
    printf("List after sorting: ");
    printArray(dstArray, 10);
    return 0;
}
