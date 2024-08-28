//Question 1
#include <stdio.h>

void addArrays(int arr1[], int arr2[], int result[]) {
    int size = 4;
    for(int i = 0; i < size; i++) {
        result[i] = arr1[i] + arr2[i];
    }
}

int main() {
    int arr1[] = {11, 22, 33, 44};
    int arr2[] = {5, 7, 9, 10};
    int result[4];

    addArrays(arr1, arr2, result);

    for(int i = 0; i < 4; i++) {
        printf("%d ", result[i]);
    }

    return 0;
}

