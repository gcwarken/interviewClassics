// Reverse words in a given string - c implementation

#include <stdio.h>
#include <string.h>

int main() {
    char myString[] = "never gonna give you up";
    int i;
    int j = strlen(myString);
    char reversedWords[j];
    int revIndex = 0;
    int revCount = 1;

    for (i = j-1; i >= -1; i--) {
        if (myString[i] == ' '|| i == -1) {
            for (revIndex; revCount < j-i; revIndex++) {
                reversedWords[revIndex] = myString[i + revCount];
                revCount++;
            }
            if (i >= 0) {
                reversedWords[revIndex] = ' ';
            }
            revIndex++;
            revCount = 1;
            j = i;
        }
    }

    printf("Original string: %s\n", myString);
    printf("String with words reversed: %s", reversedWords);

    return 0;
}