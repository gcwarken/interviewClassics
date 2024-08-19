# Given a string S, find all substrings S1 and replace by string S2 - python implementation

def findReplace(originalString, find, replace):

    newString = ""
    i = 0
    j = 0
    foundIt = False

    while (i < len(originalString)):

        if (len(find)) == 1 and originalString[i] == find:
            foundIt = True

        if len(find) > 1:
            while (originalString[i+j] == find[j]) and (j < len(find)-1):
                j = j+1
            if j == len(find)-1: foundIt = True

        if (foundIt):
            newString = newString + replace
            i = i + len(find)
        else:
            newString = newString + originalString[i]
            i = i + 1

        j = 0
        foundIt = False

    return newString

## A better aproach

def betterFindReplace(originalString, find, replace):
    newString = ""
    i = 0
    j = 0

    while (i < len(originalString) - len(find)):
        while (j < len(find) and originalString[i + j] == find[j]):
            j += 1

        if (j == len(find)):
            newString += replace
            i += j
        else:
            newString += originalString[i]
            i +=1

        j = 0

    newString += originalString[i:]
    return newString


myString = "They're taking the hobbits to Isengard."
f = "hobbits"
r = "orcs"

print(f"Original string: {myString}")
print(f"Find substring: {f}")
print(f"Replace with: {r}")
print(f"New string: {betterFindReplace(myString, f, r)}")