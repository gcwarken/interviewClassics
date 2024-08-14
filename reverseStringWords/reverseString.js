// Reverse words in a given string - javascript implementation

function reverseStringWords(s){
    let reversedWords = ""
    let j = s.length
    for (i = s.length-1; i >= 0; i--){
        if (s[i] == " ") {
            reversedWords += s.slice(i+1,j) + " ";
            j = i;
        } else if (i == 0) {
            reversedWords += s.slice(i,j);
        }
    }
    return reversedWords;
}

let s = "the words of this sentence are reversed"

console.log(`Original string: ${s}`);
console.log(`String with words reversed: ${reverseStringWords(s)}`);