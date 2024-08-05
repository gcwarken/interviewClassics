#include <stdio.h>
#include <string.h>

int main() {
    char palString[64];
    int i;
    int isPalindrome = 1;

    printf("Enter a string to check if it is a palindrome: ");
    scanf("%s", palString);

    i = 0;

    while (i <= strlen(palString) / 2) {
        printf("Comparing %c and %c\n", palString[i], palString[strlen(palString) - i-1]);

        if (palString[i] != palString[strlen(palString) - i-1]) {
            isPalindrome = 0;
            break;
        }
        i++;
    }

    if (isPalindrome){
        printf("String %s is a palindrome.\n", palString);
    }
    else {
        printf("String %s is not palindrome.\n", palString);
    }

    return 0;
}