## Questions 1 and 2
## Check line 30 to change the answered question.

from timeit import default_timer as timer
start = timer()

def quickSort(cls):
    less = []
    pivotList = []
    more = []
    class_length = len(cls)
    if class_length <= 1:
        return cls
    else:
        pivot = cls[0].ratio
        for k in range(0, class_length):
            i = cls[k].ratio
            if i < pivot:
                less.append(cls[k])
            elif i > pivot:
                more.append(cls[k])
            else:
                pivotList.append(cls[k])
        less = quickSort(less)
        more = quickSort(more)
        pivotList = sorted(pivotList, key = lambda job: job.weight, reverse=True)
        return more + pivotList + less

class job:
	def __init__(self, weight, length):
		self.weight = weight
		self.length = length
		self.ratio = weight / length # For question 1, replace division with subtraction
	def __repr__(self):
		return repr((self.weight, self.length, self.ratio))

job_objects = []
with open('3 - 1 - Minimum Completion Time - Prims Minimum Spanning Tree 1.txt') as f:
	num_of_jobs = int(f.readline())
	for line in f:
		temp = line.split()
		job_objects.append(job(int(temp[0]), int(temp[1])))

job_objects = quickSort(job_objects)
total = 0
length_total = 0

for k in range(0, num_of_jobs):
	length_total += job_objects[k].length
	total += job_objects[k].weight * length_total

print(total)

end = timer()
print("Questions 1 and 2 took", round(end - start, 1), "seconds.")

# Answer: 69119377652
# Answer: 67311454237

## Question 3

from timeit import default_timer as timer
start = timer()

import math

class edge:
	def __init__(self, vert1, vert2, cost):
		self.vert1 = vert1
		self.vert2 = vert2
		self.cost = cost
	def __repr__(self):
		return repr((self.vert1, self.vert2, self.cost))

edge_objects = []
with open('3 - 1 - Minimum Completion Time - Prims Minimum Spanning Tree 2.txt') as f:
	temp = f.readline().split()
	num_of_nodes, num_of_edges = int(temp[0]), int(temp[1])
	for line in f:
		temp = line.split()
		edge_objects.append(edge(int(temp[0]), int(temp[1]), int(temp[2])))

visited = [True] * 2 + [False] * (num_of_nodes - 1)
total_cost = 0

for x in range(0, num_of_nodes):
	dist = math.inf
	for i in range(0, num_of_edges):
		if visited[edge_objects[i].vert1] ^ visited[edge_objects[i].vert2]:
			if edge_objects[i].cost < dist:
				dist = edge_objects[i].cost
				temp = i
	if dist < math.inf:
		total_cost += dist
		visited[edge_objects[temp].vert1] = True
		visited[edge_objects[temp].vert2] = True

print(total_cost)

end = timer()
print("Question 3 took", round(end - start, 1), "seconds.")

# Answer: -3612829