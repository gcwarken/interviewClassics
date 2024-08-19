// Given a string S, find all substrings S1 and replace by string S2 - javascript implementation

function findReplace(originalString, find, replace) {
    let newString = "";
    let i = 0;
    let j = 0;

    while (i < (originalString.length) - find.length) {
        while ( (originalString[i+j] == find[j]) && (j < find.length) ) {
            j++;
        }

        if (j == find.length) {
            newString += replace;
            i += j;
        } else {
            newString += originalString[i];
            i++;
        }
        j = 0;
    }
    newString += originalString.slice(i);
    return newString;
}

let myString = "They're taking the hobbits to Isengard.";
let f = "hobbits";
let r = "orcs";

console.log(findReplace(myString, f, r));