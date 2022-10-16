# 2 - 1 - Kosaraju's SCC Algorithm is used to solve the problem by creating a
# graph and analyzing its strongly connected components with the algorithm.

# change the name of the file in each case
with open("4 - 4 - 2-SAT Problem 1.txt") as f:
	num_var = int(f.readline())
	num_nodes = num_var * 2 + 1
	gr = [[] for i in range(num_nodes)]
	r_gr = [[] for i in range(num_nodes)]
	for line in f:
	    items = line.split()
	    gr[num_var - int(items[0])] += [num_var + int(items[1])]
	    gr[num_var - int(items[1])] += [num_var + int(items[0])]
	    r_gr[num_var + int(items[0])] += [num_var - int(items[1])]
	    r_gr[num_var + int(items[1])] += [num_var - int(items[0])]

print("Graph is imported.")

visited = [False] * num_nodes
pass_thro = [False] * num_nodes # Nodes are popped from the stack in the second pass through
scc = [0] * num_nodes
stack = []  # Stack for DFS
ordering = []  # The finishing orders after the first pass

for node in range(0, num_nodes):
	if visited[node] == False:
		stack = [node]
		while stack:
			v = stack[-1]
			if pass_thro[v] == True:
				stack.pop()
				ordering.append(v)
			else:
				pass_thro[v] = True
			if visited[v] == False:
				visited[v] = True
				for head in r_gr[v]:
					if visited[head] == False:
						stack.append(head)

print("Ordering is completed.")

visited = [False] * num_nodes  # Resetting the visited variable
ordering.reverse()  # The nodes should be visited in reverse finishing times
leader = list(i for i in range(0,num_nodes + 1))

for node in ordering:
	if visited[node] == False:
		stack = [node]
		while stack:
			v = stack.pop()
			if visited[v] == False:
				visited[v] = True
				leader[v] = node
				for head in gr[v]:
					if visited[head] == False:
						stack.append(head)

flag = 0
for x in range(1,num_var + 1):
	if leader[num_var - x] == leader[num_var + x]:
		flag = 1
		print("0")
		break

if flag == 0:
	print("1")

# Answer 1: 1
# Answer 2: 0
# Answer 3: 1
# Answer 4: 1
# Answer 5: 0
# Answer 6: 0
# Answer: 101100
