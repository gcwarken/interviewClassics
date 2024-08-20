// Given a string S, find all substrings S1 and replace by string S2 - c implementation

#include <stdio.h>
#include <string.h>

int main() {
   int i = 0;
   int j = 0;
   char originalString[] = "They're taking the hobbits to Isengard.";
   char find[] = "hobbits";
   char replace[] = "orcs";
   char newString[1000];
   char temp[2];

    temp[1] = '\0';

    while (i < strlen(originalString)) {
        while ((j < strlen(find)) && (originalString[i+j] == find[j])) {
            j++;
        }

        if (j == strlen(find)) {
            strcat(newString, replace);
            i += j;
        }
        else {
            temp[0] = originalString[i];
            strcat(newString, temp);
            i++;
        }

        j = 0;
    }

    strcat(newString, "\0");

    printf("Original string: %s\n", originalString);
    printf("Find substring: %s\n", find);
    printf("Replace with: %s\n", replace);
    printf("New string: %s\n", newString);
    
    return 0;
}