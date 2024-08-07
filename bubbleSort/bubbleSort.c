// Bubble Sort algorithm - c implementation

#include <stdio.h>

void printArray(int arr[], int arrLen){
    int i;
    for (i = 0; i < arrLen; i++){
        if (i < arrLen-1) {
            printf("%d, ", arr[i]);
        } else {
            printf("%d\n", arr[i]);
        }
    }
}

void bubbleSort(int arr[], int arrLen) {
    int i, j, temp;
    int passes = 0;
    int comparisons = 0;
    int swap = 1;

    i = 0;
    while (i < arrLen && swap) {
        swap = 0;
        for (j = 0; j < arrLen - i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swap++;
            }
            comparisons++;
        }
        passes++;
        i++;
    }    
    printf("Sorted array: ");
    printArray(arr, arrLen);
    printf("%d comparisons in %d passes.", comparisons, passes);

}

int main() {
    int myArray[] = {1,4,2,3,0,5,6,7,8};
    int arrayLength = sizeof(myArray) / sizeof(myArray[0]);

    printf("Original array: ");
    printArray(myArray, arrayLength);

    bubbleSort(myArray, arrayLength);
    
    return 0;
}