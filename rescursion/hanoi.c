#include <stdio.h>


#define SIZE 10



void hanoi(int source[], int aux[], int destination[], const int size)
{
    int i = 0;

    if (size <= 0)
    {
        return;
    }
    else if (1 == size)
    {
        destination[0] = source[0];
        source[0] = 0;
    }
    else
    {
        i = size - 1;
        hanoi(source, destination, aux, size-1);
        destination[i] = source[i];
        hanoi(aux, source, destination, size-1);
    }
}

void display(const int tower[])
{
    int i = 0;
    for (i=0; i<SIZE; i++)
    {
        printf("%d ", tower[i]);
    }
    printf("\n");
}

int main()
{
    int source[SIZE] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int aux[SIZE] = {0};
    int destination[SIZE] = {0};

    display(source);
    hanoi(source, aux, destination, SIZE);
    display(destination);

    return 0;
}
