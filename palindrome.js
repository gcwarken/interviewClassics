// Palindrome algorithm - javascript implementation

function palindrome(palString) {
    let i = 0;
  
    palString = palString.replace(/\s/g, '');
    //palString = palString.split(" ").join("");
    
    while (i <= palString.length / 2) {
        console.log(`Comparing ${palString[i]}  and  ${palString[palString.length - i - 1]}`);
        if (palString[i] != palString[palString.length - i - 1]) {
            return false
        }
        i++;
    }

    return true;
};

console.log(palindrome("l  kjhghjkl"))