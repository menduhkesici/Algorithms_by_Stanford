# Floyd-Warshall Algorithm is used.
import math

# name of the text file is changed in each step
with open("4 - 1 - All-Pairs Shortest-Path - g1.txt") as f:
	temp = f.readline().split()
	num_of_vert, num_of_edges = int(temp[0]), int(temp[1])
	print(num_of_vert)
	A = [[0 for i in range(num_of_vert + 1)] for i in range(num_of_vert + 1)]
	for i in range(1,num_of_vert + 1):
		for j in range(1,num_of_vert + 1):
			A[i][j] = math.inf
	for i in range(1, num_of_vert + 1):
		A[i][i] = 0
	for line in f:
		temp = line.split()
		A[int(temp[0])][int(temp[1])] = int(temp[2])
		
B = [[0 for i in range(num_of_vert + 1)] for i in range(num_of_vert + 1)]

for k in range(1,num_of_vert + 1):
	print(round(k / num_of_vert * 100, 1), "% completed.")
	for i in range(1,num_of_vert + 1):
		for j in range(1,num_of_vert + 1):
			B[i][j] = min(A[i][j], (A[i][k] + A[k][j]))
	A = B

# negative cycle checker
flag = 0
for i in range(1,num_of_vert + 1):
	if B[i][i] < 0:
		flag = 1
		break

if flag == 1:
	print("NULL")
else:
	shortest = math.inf
	for i in range(1,num_of_vert + 1):
		for j in range(1,num_of_vert + 1):
			if B[i][j] < shortest:
				shortest = B[i][j]
	print(shortest)

# for g1: NULL
# for g2: NULL
# for g3: -19
# Answer: -19