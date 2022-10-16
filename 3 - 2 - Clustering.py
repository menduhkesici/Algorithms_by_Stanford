## Question 1

class edge:
	def __init__(self, vert1, vert2, cost):
		self.vert1 = vert1
		self.vert2 = vert2
		self.cost = cost
	def __repr__(self):
		return repr((self.vert1, self.vert2, self.cost))

edge_object = []
with open('3 - 2 - Clustering 1.txt') as f:
	num_of_nodes = int(f.readline())
	for line in f:
		temp = line.split()
		edge_object.append(edge(int(temp[0]), int(temp[1]), int(temp[2])))

edge_object = sorted(edge_object, key = lambda edge: edge.cost)

k = 4
cluster = num_of_nodes
i = 0
leader = list(range(0, num_of_nodes + 1))
num_of_elements = [0] * (num_of_nodes + 1)

while cluster > k:
	vert1 = edge_object[i].vert1
	vert2 = edge_object[i].vert2
	if leader[vert1] != leader[vert2]:
		cluster -= 1
		if num_of_elements[vert1] >= num_of_elements[vert2]:
			leader1 = leader[vert1]
			leader2 = leader[vert2]
		else:
			leader1 = leader[vert2]
			leader2 = leader[vert1]
		for m in range(1, num_of_nodes + 1):
			if leader[m] == leader2:
				leader[m] = leader1
	i += 1

while True:
	vert1 = edge_object[i].vert1
	vert2 = edge_object[i].vert2
	if leader[vert1] != leader[vert2]:
		print(edge_object[i].cost)
		break
	else:
		i += 1

# Answer: 106

## Question 2

def neighbors(x):
    result = []
    for i in numbers:
        if leader[x^i] != 0: # Eliminates the numbers not entered
            result.append(x^i)
    return result

with open("3 - 2 - Clustering 2.txt") as f:
    temp = f.readline().split()
    num_of_nodes, num_of_bits = int(temp[0]), int(temp[1])
    leader = [0] * pow(2, num_of_bits)
    index = []
    count = 1
    for line in f:
        temp = int(line.replace(' ',''), base = 2)
        index.append(temp)
        leader[temp] = count
        count += 1

numbers = [0] * int(num_of_bits * (num_of_bits + 1) / 2)
k = 0
for i in range(num_of_bits):
    for j in range(i, num_of_bits):
        numbers[k] = (1 << i) | (1 << j)
        k += 1

cluster_leaders = []
for i in index:
    if leader[i] not in cluster_leaders:
	    cluster_leaders.append(leader[i])
	    cluster = [i]
	    while len(cluster) != 0:
	        cluster2 = []
	        for x in cluster:
	            for y in neighbors(x):
	                if leader[y] != leader[i]:
	                    cluster2.append(y)
	                    leader[y] = leader[i]
	        cluster = cluster2

print(len(cluster_leaders))

# Answer: 6118