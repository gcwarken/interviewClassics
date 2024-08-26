    // Given a string, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
    // C implementation

    #include <stdio.h>
    #include <string.h>

    int main () {
        char s[] = "abcabcabc";
        int subPatLength, j;
        int isRepeat = 0; // 0 = false

        subPatLength = strlen(s) / 2;
        while (subPatLength > 0  && !isRepeat) {
            if (strlen(s) % (subPatLength) == 0) {
                j = 0;
                while (s[j] == s[j % subPatLength] && j < strlen(s)) {
                    j++;
                }
            }
            if (j == strlen(s)) {
                isRepeat++;
            }
            subPatLength--;
        }

        if (isRepeat) {
            printf("String %s IS composed of reapeating subpattern.\n", s);
        } else {
            printf("String %s IS NOT not composed of reapeating subpattern.\n", s);
        }

        return 0;
    }