def sort_and_count(list):
	if len(list) == 1:
		return (list, 0)
	else:
		middle = len(list) // 2
		left = list[:middle]
		right = list[middle:]
		(left, x) = sort_and_count(left)
		(right, y) = sort_and_count(right)
		(list, z) = count_split_inv(left, right)
	return (list, x + y + z)

def count_split_inv(left, right):
	result = []
	x = 0
	left_idx, right_idx = 0, 0
	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx] <= right[right_idx]:
			result.append(left[left_idx])
			left_idx += 1
		else:
			result.append(right[right_idx])
			right_idx += 1
			x = x + len(left) - left_idx
	if left:
		result.extend(left[left_idx:])
	if right:
		result.extend(right[right_idx:])
	return (result, x)

print("Enter the numbers (seperated by spaces):")
a = [int(x) for x in input().split()]
print(sort_and_count(a)[1])

## use this part if numbers are seperated by 'Enter' (put -1 to the end of the list)
a = []
x = 0

while (x != -1):
	x = int(input())
	a.append(x)

del a[len(a)-1]

print(sort_and_count(a)[1])

input()

# Answer: 2407851245