// Given a string, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
// Javascript implementation

function repPattern(s){
    let i, j = 0;
    let intHalf = (s.length - (s.length % 2)) / 2;
    let subPat = s.slice(0,intHalf);

    if (s.length === 1) {return true};

    for (i = intHalf; i >= 0; i--) {
        if (s.length % subPat.length == 0) {
            while (j < s.length && s[j] == subPat[j % subPat.length]) {
                j++;
            }
            if (j == s.length) {return true}
        }
        j = 0;
        subPat = s.slice(0,i);
    }

    return false;
}

console.log(repPattern("abcabcabc"));