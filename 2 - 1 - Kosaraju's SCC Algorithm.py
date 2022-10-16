
########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator. range(875715) goes up to 875714.
num_nodes = 11

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
ordering = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("2 - 1 - Kosaraju\'s SCC Algorithm_test.txt", "r")
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]

print("Graph is imported.")

########################################################
# DFS on reverse graph
visited = [False] * num_nodes
pass_thro = [False] * num_nodes # Nodes are popped from the stack in the second pass through

for node in range(1, num_nodes):
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

########################################################
# DFS on original graph

visited = [False] * num_nodes  # Resetting the visited variable
ordering.reverse()  # The nodes should be visited in reverse finishing times
scc = []
for node in ordering:
	if visited[node] == False:
		scc.append(0)
		stack = [node]
		while stack:
			v = stack.pop()
			if visited[v] == False:
				visited[v] = True
				scc[-1] += 1
				for head in gr[v]:
					if visited[head] == False:
						stack.append(head)

########################################################
# Getting the five biggest sccs
scc.sort(reverse=True)
print(scc[:5])

# Answer: 434821,968,459,313,211