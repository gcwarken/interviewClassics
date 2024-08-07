# Bubble Sort algorithm - python implementation

def bubbleSort(arr):
    print("Simple bubble sort:")
    print("\tOriginal array: " + str(arr))

    passes = 0
    comparisons = 0

    for i in range(len(arr)):
        for j in range(len(arr) - i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            comparisons += 1
        passes += 1

    print("\tSorted array: " + str(arr))
    print(f"\t{str(comparisons)} comparisons in {str(passes)} passes.")

## a better aproach, breaks if no swaps are made
def bubbleSortCheckIfSwap(arr):
    print("Bubble sort breaking if no swaps occur:")
    print("\tOriginal array: " + str(arr))
    
    passes = 0
    comparisons = 0
    swap = True

    i = 0
    j = 0

    while (i < len(arr) and swap):
        swap = False
        for j in range(len(arr) - i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
            comparisons += 1
        passes += 1
        i += 1

    print("\tSorted array: " + str(arr))
    print(f"\t{str(comparisons)} comparisons in {str(passes)} passes.")

## Call functions ##############################################################
bubbleSort([1,4,2,3,0,5,6,7,8])
bubbleSortCheckIfSwap([1,4,2,3,0,5,6,7,8])