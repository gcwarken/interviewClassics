// Print array after it is right rotated K times - javascript implementation

function rightRotation(a, k) {
    // rotate array a to the right k times
    let rotations = k % a.length;
    let rotatedArray = [];

    for (i = rotations; i < a.length; i++) {
        rotatedArray.push(a[i]);
    }

    for (i = 0; i < rotations; i++) {
        rotatedArray.push(a[i]);
    }

    console.log(`Original array: ${a}`);
    console.log(`Array after ${k} right rotations: ${rotatedArray}`);
}

rightRotation([1,2,3,4,5,6,7,8,9],4);