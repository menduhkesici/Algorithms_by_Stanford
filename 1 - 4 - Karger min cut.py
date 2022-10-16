import random
import math

all_min_cut = math.inf

w, h = 0, 200;

vert = [[0 for x in range(w)] for y in range(h)] 

x = 0

with open('1 - 4 - Karger min cut.txt') as f:
	for line in f:
		vert[x] = [int(i) for i in line.split()]
		del vert[x][0]
		x = x + 1

for count in range(1,201):
	
	edges = []

	for x in range(0,200):
		for y in range(0,len(vert[x])):
			if x < vert[x][y]:
				edges.append([x + 1, vert[x][y]])

	min_cut = len(edges)

	for y in range(0,198):
		edge_rand = random.randint(0,len(edges)-1)
		ver_1 = edges[edge_rand][0]
		ver_2 = edges[edge_rand][1]
		del edges[edge_rand]
		for z in range(0,len(edges)):
			if edges[z][0] == ver_2:
				edges[z][0] = ver_1
			if edges[z][1] == ver_2:
				edges[z][1] = ver_1
		for z in range(len(edges)-1,-1,-1):
			if edges[z][0] == edges[z][1]:
				del edges[z]
	if len(edges) < min_cut:
		min_cut = len(edges)

	print(count, min_cut)
	if all_min_cut > min_cut:
		all_min_cut = min_cut

print()
print(all_min_cut)

input()

# Answer: 17