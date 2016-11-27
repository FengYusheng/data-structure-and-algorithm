#include<stdio.h>

#define MAX 10

int srcArray[MAX] = {10, 14, 19, 26, 27, 31, 33, 35, 42, 44};

int interpolation_search(int src[], int len, int value) {
    int low = 0;
    int high = len - 1;
    int mid = -1;
    int i = 0;

    if (high < low) {
        return -1;
    }

    mid = low + ((double)(high - low) / (src[high] - src[low])) * (value - src[low]);
    printf("compared %d#:\n", i);
    printf("low is %d\nhigh is %d\nmid is %d\n", low, high, mid);
    printf("src[low] is %d\nsrc[high] is %d\nsrc[mid] is %d\n", src[low], src[high], src[mid]);

    while (src[mid] != value) {
        i++;

        if (value == src[mid]) {
            printf("Element found at location %d\n", mid);
            break;
        } else if (src[mid] < value) {
            high = mid;
        } else {
            low = mid;
        }

        if (high == low) {
            if (value != src[low]) {
                printf("%d is not found\n", value);
                mid = -1;
                break;
            }
        } else {
            mid = low + ((high - low) / (src[high] - src[low])) * (value - src[low]);
        }

        printf("compared %d#:\n", i);
        printf("low is %d\nhigh is %d\nmid is %d\n", low, high, mid);
        printf("src[low] is %d\nsrc[high] is %d\nsrc[mid] is %d\n",src[low], src[high], src[mid]);
    }

    return mid;
}


int main() {
    int location;
    location = interpolation_search(srcArray, MAX, 33);
    printf("33 is at location %d\n", location);
    return 0;
}
