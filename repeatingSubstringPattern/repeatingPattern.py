# Given a string, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
# Python implementation

def repPattern(s):
    half = len(s) // 2
    subPat = s[0:half]
    j = 0

    if len(s) == 1: return True

    for i in range(half, 1, -1):
        if len(s) % len(subPat) == 0:
            while ( j < len(s) and s[j] == subPat[j % len(subPat)]):
                j += 1
            if (j == len(s)): return True
        j = 0
        subPat = s[0:i]

    return False

print(repPattern("abcabcabc"))