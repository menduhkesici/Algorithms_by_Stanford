import math

cities = []

with open("4 - 3 - Travelling Salesman (Nearest Neighbor).txt") as f:
	num_of_cities = int(f.readline())
	for line in f:
		temp = line.split()
		cities.append([float(temp[1]), float(temp[2])])

visited = [False] * num_of_cities
visited[0] = True
curr_city = 0
total_dist = 0

for k in range(num_of_cities - 1):
	closest_dist_sq = math.inf
	closest_city = 0
	i = curr_city
	for j in range(1,num_of_cities):
		if (visited[j] == False):
			dist_sq = (cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2
			if (dist_sq < closest_dist_sq):
				closest_dist_sq = dist_sq
				closest_city = j
	if (closest_city != 0):
		total_dist += closest_dist_sq**0.5
		visited[closest_city] = True
		curr_city = closest_city
	# to show progress
	if (k % 100 == 0):
		print(round(k / num_of_cities * 100, 2), "% completed.")

total_dist += ((cities[0][0] - cities[curr_city][0])**2 + (cities[0][1] - cities[curr_city][1])**2)**0.5

print(total_dist)

# Answer: 1203406