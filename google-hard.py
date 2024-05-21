"""Good morning! Here's your coding interview
 problem for today.

This problem was asked by Google.
Given an array of strictly the characters 'R', 'G',
and 'B', segregate the values of the array so that all
the Rs come first, the Gs come second,
and the Bs come last. You can only swap
elements of the array.

Do this in linear time and in-place.

For example, given the array 
['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def arrange(L):
	R = 0
	G = 1
	B = 2

	for i in range(len(L)):
		current = L[i]
		if current == "R" and L[R] != "R":
			temp = L[R]
			L[R] = current
			L[i] = temp

		elif current == "R":
			for j in range(i,R,-1):
				L[j] = L[j-1]

			L[R] = current
			R += 1

			B += 1
			G += 1

		elif current == "R" and R == i:
			R += 1
			continue

		if L[G] != "G" and current == "G":
			temp = L[G]
			L[G] = current
			L[i] = temp


		elif current == "G":
			for j in range(i,G,-1):
				L[j] = L[j-1]

			L[G] = current
			G += 1


		elif current == "G" and G == i:
			G += 1
			continue

		if current == "B" and L[B] != "B":
			temp = L[B]
			L[B] = current
			L[i] = temp

		elif current == "B":
			for j in range(i,B,-1):
				L[j] = L[j-1]
			L[B] = current
			B += 1

		elif current == "B" and B == i:
			B += 1
			continue
	return L

print(arrange(["B","G","R","R","B","R","G"]))

print(arrange(["B","R","G","R","R","G","B"]))
print(arrange(["R","B","B","R","G","R"]))
