// Bubble Sort algorithm - javascript implementation

function bubbleSort(arr) {
    let i, j, temp;
    
    console.log(`Original array: ${arr}`);

    for (i = 0; i < arr.length; i++) {
        for (j = 0; j < arr.length - i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    console.log(`Sorted array: ${arr}`);
}

bubbleSort([5,1,8,2,7,6,3,0,4])