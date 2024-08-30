// Find all string subsequences
// Javascript implementation

function getAllSubseq(s) {
    // using binary to select individual chars
    let combinations = (2 ** s.length) - 1; // binary of 1's with string's length
    let subSeqs = [];
    let tempString;
    let i, j;

    for (combinations; combinations > 0; combinations--) {
        i = combinations;
        j = 0;
        tempString = `${i.toString(2)}: `; // store the binary as well for clarity
        while (i > 0) {
            if (i & 1) {
                tempString += s[j];
            }
            j++;
            i = i >> 1 // right shift
        }
        subSeqs.push(tempString);
    }
    return subSeqs;
}

let myString = "ABCD";
console.log(getAllSubseq(myString));