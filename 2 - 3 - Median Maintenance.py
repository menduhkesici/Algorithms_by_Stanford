
import heapq

H_min = [] # values are converted to negative while heappush as the max must be on the top
H_max = [] # values remains the same while heappush as the min must be on the top
median_total = 0 # sum of subsequent medians

with open('2 - 3 - Median Maintenance.txt') as f:
	# Scan first number
	num_1 = int(f.readline())
	median_total += num_1
	# Scan second number
	num_2 = int(f.readline())
	heapq.heappush(H_min, min(num_1, num_2) * -1) 
	heapq.heappush(H_max, max(num_1, num_2))
	median_total += H_min[0] * -1
	# Scan rest of the numbers
	for line in f:
		temp = int(line)
		if temp <= (-1 * H_min[0]):
			heapq.heappush(H_min, temp * -1)
		elif temp <= H_max[0]:
			if len(H_min) <= len(H_max):
				heapq.heappush(H_min, temp * -1)
			else:
				heapq.heappush(H_max, temp)
		else:
			heapq.heappush(H_max, temp)
		if len(H_min) > len(H_max) + 1:
			popped = heapq.heappop(H_min) * -1
			heapq.heappush(H_max, popped)
		if len(H_max) > len(H_min) + 1:
			popped = heapq.heappop(H_max)
			heapq.heappush(H_min, popped * -1)
		if ((len(H_min) + len(H_max)) % 2 == 0) or (len(H_min) > len(H_max)):
			median_total += H_min[0] * -1
		else:
			median_total += H_max[0]

print(median_total % 10000)

# Answer: 1213