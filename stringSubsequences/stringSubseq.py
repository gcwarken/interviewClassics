# Find all string subsequences
# Python implementation

def getAllSubseq(s):
    subseqs = []
    tempString = ""

    for combinations in range( ((2 ** len(s)) - 1) , 0, -1):
        i = combinations
        j = 0
        tempString = bin(combinations) + ": "
        while (i > 0):
            if (i & 1):
                tempString += s[j]
            j += 1
            i = i >> 1
        subseqs.append(tempString)

    return subseqs

myString = "ABCD"
print(getAllSubseq(myString))