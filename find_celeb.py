"""
Good morning! Here's your coding interview
 problem for today.

This problem was asked by Pinterest.

At a party, there is a single person who everyone know
but who does not know anyone in
return (the "celebrity").
To help figure out who this is,
you have access to an O(1) method called knows(a, b), which returns True if person a knows person b,
else False.

Given a list of N people and the above operation
find a way to identify the celebrity in O(N) time.
"""
def knows(a,b):
	if a == 5:
		return False
	elif b == 5:
		return True

def find_celebrity(N):
	current = N[0]

	for i in range(1,len(N)):
		if knows(current,N[i]):
			if not knows(N[i],current):
				current = N[i]

		if not knows(current,N[i]):
			if knows(N[i],current):
				pass


	return current

print(find_celebrity(list(range(10))))
