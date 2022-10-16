## Questions 1 and 2

import math

def first_second_smallest(arr):
	first_index, second_index = -1, -1
	first, second = math.inf, math.inf
	for i in range(0, len(arr)):
		if arr[i] <= first:
			second = first
			second_index = first_index
			first = arr[i]
			first_index = i
		elif arr[i] <= second:
			second = arr[i]
			second_index = i
	return first_index, second_index

class tree:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.parent = None
	def __repr__(self):
		return repr((self.left, self.right, self.parent))

with open('3 - 3 - Huffman - Maximum-weight independent set 1.txt') as f:
	num_of_symbols = int(f.readline())
	tree_objects = []
	weights = []
	for line in f:
		tree_objects.append(tree(None, None))
		weights.append(int(line))

for i in range(1, num_of_symbols): # The merging will occur exactly (num_of_symbols - 1) times
	ind1, ind2 = first_second_smallest(weights)
	total_weight = weights[ind1] + weights[ind2]
	weights.append(total_weight)
	tree_objects.append(tree(ind1, ind2))
	tree_objects[ind1].parent, tree_objects[ind2].parent = (i + num_of_symbols - 1), (i + num_of_symbols - 1) 
	weights[ind1], weights[ind2] = math.inf, math.inf # Weights are cleaned to not affect future mergings

# Ranks are calculated with Breadth First Search
stack = [tree_objects[-1].left, tree_objects[-1].right]
i = 0
ranking = [0] * len(tree_objects)

while len(stack) > 0:
	node = stack.pop()
	parent = tree_objects[node].parent
	ranking[node] = ranking[parent] + 1
	if tree_objects[node].left != None:
		stack.append(tree_objects[node].left)
	if tree_objects[node].right != None:
		stack.append(tree_objects[node].right)

ranking = ranking[0:num_of_symbols]
print(max(ranking))
print(min(ranking))

# Answer: 19
# Answer: 9

## Question 3

with open('3 - 3 - Huffman - Maximum-weight independent set 2.txt') as f:
	num_of_vertices = int(f.readline())
	weights = [0]
	for line in f:
		weights.append(int(line))

A = [0]
A.append(weights[1])

for i in range(2, num_of_vertices + 1):
	A.append(max(A[i-1], A[i-2] + weights[i]))

S = []

while i >= 1:
	if A[i-1] >= (A[i-2] + weights[i]):
		i -= 1
	else:
		S.append(i)
		i -= 2

for i in (1, 2, 3, 4, 17, 117, 517, 997):
	if i in S:
		print("1", end="")
	else:
		print("0", end="")
print()

# Answer: 10100110
