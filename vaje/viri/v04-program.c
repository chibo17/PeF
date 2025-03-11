// C program for implementation of selection sort
#include <stdio.h>

void selectionSort(int arr[], int N) {

    // Start with the whole array as unsored and one by
      // one move boundary of unsorted subarray towards right
    for (int i = 0; i < N - 1; i++) {

        // Find the minimum element in unsorted array
        int min_idx = i;
        for (int j = i + 1; j < N; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        // Swap the found minimum element with the first
        // element in the unsorted part
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int N = sizeof(arr) / sizeof(arr[0]);
    printf("Unsorted array: \n");
    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
  
      // Calling selection sort
    selectionSort(arr, N);

    printf("Sorted array: \n");
    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}