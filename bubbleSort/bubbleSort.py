# Bubble Sort algorithm - python implementation

def bubbleSort(arr):
    print("Original array: " + str(arr))
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            # print("Comparing " + str(arr[j]) + " and " + str(arr[j+1]))
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array: " + str(arr))

bubbleSort([5,1,8,2,7,6,3,0,4])