#include <stdio.h>
#include <stdlib.h>

// ❌ Memory leak: No free() for allocated memory
void memoryLeak() {
    int *arr = (int*)malloc(5 * sizeof(int));
    arr[0] = 10; // No free(arr), causes memory leak
}

// ❌ Logical bug: Wrong condition (should be `x < y`)
int findMin(int x, int y) {
    if (x > y) {  // Bug: should be x < y
        return y;
    } else {
        return x;
    }
}

// ❌ Uninitialized variable usage
void uninitializedVariable() {
    int a;
    printf("Value of a: %d\n", a); // 'a' is not initialized, undefined behavior
}

// ❌ Infinite loop: Incorrect loop condition
void infiniteLoop() {
    int i = 0;
    while (i >= 0) { // Loop runs forever
        printf("%d\n", i);
        i++; // Should have a stopping condition
    }
}

// ❌ Division by zero error
void divisionByZero() {
    int x = 10;
    int result = x / 0; // Crashes program
    printf("Result: %d\n", result);
}

int main() {
    memoryLeak();
    printf("Min: %d\n", findMin(10, 5));
    uninitializedVariable();
    infiniteLoop();  // Uncommenting this will cause an infinite loop
    divisionByZero(); // Uncommenting this will cause a crash
    return 0;
}
