"""
Good morning! Here's your coding interview problem for
today.

This problem was asked by Twitter.

A classroom consists of N students,
whose friendships can be represented in an adjacency list.
For example, the following descibes a situation where 0 
is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can
be defined as the transitive closure of that student's 
friendship relations.
In other words,
this is the smallest set such that no student in 
the group has any friends outside this group.
For the example above, the friend groups would be
{0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above,
determine the number of friend groups in the class."""

def find_group(D):
	keys = list(D.keys())
	results = []

	for index in range(len(keys)):
		key = keys[index]
		result = D[key] + [key]
		flag = False

		for friends_group in results:
			if key in friends_group:
				flag = True
				break
			else:
				flag = False

		if flag: continue
		for index2 in range(index,len(keys)):
			key2 = keys[index2]
			friends = D[key2]

			if key in friends:
				for friend in friends:
					if friend not in result:
						result.append(friend)
		results.append(result)

	return results
print(find_group({0:[1,2],
  1:[0,5],
  2:[0],
  3:[6],
  4:[],
  5:[1],
  6:[3]
}))
