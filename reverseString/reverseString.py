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


s = "the words of this sentence are reversed"

print(f"Original sring: {s}")
print(f"String with words reversed: {reverseStringWords(s)}")
