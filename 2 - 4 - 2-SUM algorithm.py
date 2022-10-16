values = []
h = {}

with open('2 - 4 - 2-SUM algorithm_test.txt') as f:
	for line in f:
		values.append(int(line))
		h[int(line)] = True

num_t = 0

for t in range(-10000, 10001):
	for x in values:
		if (t - x) in h:
			if x != t / 2:
				num_t += 1
				#print(t, x, (t - x))
				break

print(num_t)

# Answer: 427