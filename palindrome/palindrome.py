# Palindrome algorithm - python implementation

checkPal = input("Enter a string to check if it is a palindrome: ")
i = 0
palindrome = True

# trim whitespace with replace
# checkPalTrimmed = checkPal.replace(' ', '')

# trim whitespace whithout replace
checkPalTrimmed = ""
for char in checkPal:
	if char != ' ':
		checkPalTrimmed += char

# compare chars
while i < (len(checkPalTrimmed))/2:
	if checkPalTrimmed[i] != checkPalTrimmed[-(i+1)]:
		palindrome = False
		break
	i += 1

if palindrome:
	print("Input string is a palindrome")
else:
	print("Input string is not a palindrome")