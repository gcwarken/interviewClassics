# Reverse words in a given string - python implementation

def reverseString(s):
    reverse = ""
    for i in range(len(s)):
        reverse = reverse + s[len(s)-i-1]
    return reverse

def reverseStringWords(myString):
    myString = reverseString(myString)
    reversedWords = ""

    j = 0
    for i in range(len(myString)):
        if (myString[i] == " "):
            reversedWords = reversedWords + reverseString(myString[i-j:i]) + myString[i]
            j = 0
        elif (i == len(myString)-1):
            reversedWords = reversedWords + reverseString(myString[i-j:i+1])
            j = 0
        else:
            j = j + 1

    return reversedWords

## A better approach
def betterReverseStringWords(s):
    reversedWords = ""
    j = len(s)
    for i in range(len(s)-1, -1, -1):
        if (s[i] == " "):
            reversedWords = reversedWords + s[i+1:j] + " "
            j = i
        elif (i == 0):
            reversedWords = reversedWords + s[i:j]

    return reversedWords

s = "never gonna give you up"

print(f"Original sring: {s}")
print(f"String with words reversed: {betterReverseStringWords(s)}")