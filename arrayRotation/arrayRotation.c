// Print array after it is right rotated K times - c implementation

#include <stdio.h>
#include <stdlib.h>

int main() {
    int k, rotations;
    int i, j;
    int arraySize;
    int* myArray;
    int* rotatedArray;

    printf("Enter array size: ");
    scanf("%d", &arraySize);

    printf("Enter number of rotations: ");
    scanf("%d", &k);

    // populate array
    myArray = (int*)malloc(arraySize * sizeof(int));
    for (i = 0; i < arraySize; i++) {
        myArray[i] = i+1;
    }

    // rotate
    rotations = k % arraySize;
    rotatedArray = (int*)malloc(arraySize * sizeof(int));
    j = 0;

    for (i = rotations; i < arraySize; i++) {
        rotatedArray[j] = myArray[i];
        j++;
    }

    for (i = 0; i < rotations; i++) {
        rotatedArray[j] = myArray[i];
        j++;
    }

    // print arrays
    printf("Original array: ");
    for (i = 0; i < arraySize; i++) {
        printf("%d ", myArray[i]);
    }

    printf("\nArray after %d rotations: ", k);
    for (i = 0; i < arraySize; i++) {
        printf("%d ", rotatedArray[i]);
    }

    free(myArray);
    free(rotatedArray);
    
    return 0;
}
