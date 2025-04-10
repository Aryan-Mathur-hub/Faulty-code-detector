#include <stdio.h>
#include <stdlib.h>

void allocateAndFree() {
    int *arr = (int *)malloc(5 * sizeof(int));
    if (arr != NULL) {
        arr[0] = 10;
        printf("First element: %d\n", arr[0]);
        free(arr);
    } else {
        printf("Memory allocation failed\n");
    }
}

int findMin(int x, int y) {
    if (x < y) {
        return x;
    } else {
        return y;
    }
}

void initializedVariable() {
    int a = 5;
    printf("Value of a: %d\n", a);
}

void safeLoop() {
    for (int i = 0; i < 5; i++) {
        printf("i = %d\n", i);
    }
}

void safeDivision() {
    int x = 10, y = 2;
    if (y != 0) {
        int result = x / y;
        printf("Division result: %d\n", result);
    } else {
        printf("Cannot divide by zero\n");
    }
}

int main() {
    allocateAndFree();
    printf("Min: %d\n", findMin(10, 5));
    initializedVariable();
    safeLoop();
    safeDivision();
    return 0;
}
