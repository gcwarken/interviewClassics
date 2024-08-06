# Print array after it is right rotated K times - python implementation

n = input("Enter number of array elements: ")
while not n.isnumeric():
	n = input("That is not a number, try again: ")

k = input("Enter number of rotations: ")
while not k.isnumeric():
	k = input("That is not a number, try again: ")

n = int(n)
k = int(k)

myArray = []

for i in range(n):
	myArray.append(i)

print("Original array: " + str(myArray))

# rotate k mod n times
for i in range(k % n): 
	# rearrange array elements
	first = myArray[0]
	for j in range(len(myArray)-1):
		myArray[j] = myArray[j+1]
	myArray[-1] = first
	print("Rotation " + str(i+1) + ": " + str(myArray))

print("Rotated array: " + str(myArray))

########## A better aproach 
def rightRotation(a, k):
# rotate array a to the right k times

	rotations = k % len(a)
	rotatedArray = []

	# get elements after Kth index
	for i in range(rotations, len(a)):
		rotatedArray.append(a[i])

	# get elements before Kth index
	for i in range(0, rotations):
		rotatedArray.append(a[i])

	print("Original array: " + str(a))
	print("Rotated array: " + str(rotatedArray))
