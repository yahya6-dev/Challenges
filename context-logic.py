"""Good morning! Here's your coding interview problem
 for today.

This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus 
operators. Return the quotient as an integer,
ignoring the remainder."""

def div(denominator,numerator):
	denominator -= 1
	result =  numerator >> denominator
	return result

print(div(2,18))
print(div(2,32))
