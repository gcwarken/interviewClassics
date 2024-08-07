// Bubble Sort algorithm - javascript implementation

function bubbleSort(arr) {
    let i, j, temp;
    let passes = 0;
    let comparisons = 0;
    let swap = true;
    
    console.log(`Original array: ${arr}`);

    i = 0;
    while (i < arr.length && swap) {
        swap = false;
        for (j = 0; j < arr.length - i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swap = true;
            }
            comparisons++;
        }
        passes++;
        i++;
    }

    console.log(`Sorted array: ${arr}`);
    console.log(`${comparisons} comparisons in ${passes} passes.`);
}

bubbleSort([1,4,2,3,0,5,6,7,8]);