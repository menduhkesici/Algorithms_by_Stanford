# tsp package is used to solve the problem.
# can be installed by using the command "pip install tsp".

import tsp

cities = []

with open("4 - 2 - Travelling Salesman Problem.txt") as f:
	num_of_cities = int(f.readline())
	for line in f:
		temp = line.split()
		cities.append([float(temp[0]), float(temp[1])])

distance = [[0 for i in range(num_of_cities)] for i in range(num_of_cities)]

for i in range(0,num_of_cities):
	for j in range(0,num_of_cities):
		distance[i][j] = ((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)**0.5
	
r = range(len(distance))

dist = {(i, j): distance[i][j] for i in r for j in r}

print(tsp.tsp(r, dist))

# Answer: 26442