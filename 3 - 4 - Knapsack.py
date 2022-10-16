## Question 1

with open('3 - 4 - Knapsack 1.txt') as f:
	temp = f.readline().split()
	knapsack_size = int(temp[0]) - 1
	num_of_items = int(temp[1]) - 1
	values = []
	weights = []
	for line in f:
		temp = line.split()
		values.append(int(temp[0]))
		weights.append(int(temp[1]))

A = [[0 for x in range(knapsack_size + 1)] for y in range(num_of_items + 1)]

for i in range(1, num_of_items + 1):
	for x in range(1, knapsack_size + 1):
		if weights[i] >= x:
			A[i][x] = A[i-1][x]
		else:
			A[i][x] = max(A[i-1][x], A[i-1][x-weights[i]] + values[i])

print(A[-1][-1])

# Answer: 2493893

## Question 2

import sys

def knapsack(i, x):
	if i == -1 or x == 0:
		return 0
	if weights[i] >= x:
		if (i-1, x) not in cache:
			cache[(i-1, x)] = knapsack(i-1, x)
		return cache[(i-1, x)]
	else:
		if (i-1, x) not in cache:
			cache[(i-1, x)] = knapsack(i-1, x)
		solution_without_ith_item = cache[(i-1, x)]
		if (i-1, x-weights[i]) not in cache:
			cache[(i-1, x-weights[i])] = knapsack(i-1, x-weights[i])
		solution_with_ith_item = cache[(i-1, x-weights[i])] + values[i]
		return max(solution_with_ith_item, solution_without_ith_item)


with open('3 - 4 - Knapsack 2.txt') as f:
	temp = f.readline().split()
	knapsack_size = int(temp[0]) - 1
	num_of_items = int(temp[1]) - 1
	values = []
	weights = []
	for line in f:
		temp = line.split()
		values.append(int(temp[0]))
		weights.append(int(temp[1]))

cache = {}

sys.setrecursionlimit(2500)

print(knapsack(num_of_items, knapsack_size))

# Answer: 4243395