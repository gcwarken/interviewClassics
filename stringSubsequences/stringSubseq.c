// Find all string subsequences
// C implementation

#include <stdio.h>
#include <string.h>

int main() {
    char myString[] = "ABCD";
    int combinations = (1 << strlen(myString)) - 1;
    int i, j;

    for (combinations; combinations > 0; combinations--) {
        i = combinations;
        j = 0;
        while (i > 0) {
            if (i & 1) {
                printf("%c", myString[j]);
            }
            i = i >> 1;
            j++;
        }
        printf("\n");
    }

    return 0;
}