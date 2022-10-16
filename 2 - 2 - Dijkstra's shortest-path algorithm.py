
########################################################
# The straightforward O(mn) time implementation of Dijkstra's algorithm is used.
# Distance from 1st vertex is calculated.

import math

w, h = 0, (1 + 200);
vert = [[0 for x in range(w)] for y in range(h)]
length = [[0 for x in range(w)] for y in range(h)]
x = 1

with open('2 - 2 - Dijkstra\'s shortest-path algorithm.txt') as f:
	for line in f:
		temp = line.split()
		del temp[0]
		for y in range(0,len(temp)):
			vert[x].append(int(temp[y].split(",")[0]))
			length[x].append(int(temp[y].split(",")[1]))
		x = x + 1

visited = [True] * 2 + [False] * (h - 2)
distance = [0] * 2 + [math.inf] * (h - 2)

flag = 0
while flag == 0:
	dist = math.inf
	flag = 1
	for v in range(1, h):
		if visited[v] == True:
			len_ind = 0 # length index
			for w in vert[v]:
				if visited[w] == False:
					tmp = distance[v] + length[v][len_ind]
					if tmp < dist:
						flag = 0
						dist = tmp
						min_v = v
						min_w = w
				len_ind += 1
	if flag == 0:
		visited[min_w] = True
		distance[min_w] = dist

for x in [7,37,59,82,99,115,133,165,188,197]:
	print(distance[x], end = ',')

# Answer: 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068