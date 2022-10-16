# x: number of comparisons
def quicksort (A, f, l, x):

	if l - f <= 0:
		return x

	"""
	# for second part
	A[l], A[f] = A[f], A[l]
	"""

	"""
	# for third part
	m = f + (l - f) // 2
	if (A[f] >= A[m] and A[m] >= A[l]) or (A[l] >= A[m] and A[m] >= A[f]):
		A[m], A[f] = A[f], A[m]
	if (A[f] >= A[l] and A[l] >= A[m]) or (A[m] >= A[l] and A[l] >= A[f]):
		A[l], A[f] = A[f], A[l]
	"""

	p = A[f]
	i = f + 1

	for j in range(f+1, l+1):
		if A[j] < p:
			A[j], A[i] = A[i], A[j]
			i = i + 1

	A[i - 1], A[f] = A[f], A[i - 1]
	x1 = quicksort(A, f, i - 2, 0)
	x2 = quicksort(A, i, l, 0)

	return (x + x1 + x2 + l - f)

## use this part if numbers are separated by 'Enter' (put -1 to the end of the list)
a = []
x = 0

while (x != -1):
	x = int(input())
	a.append(x)

del a[len(a)-1]

print(quicksort(a, 0, len(a) - 1, 0))
# print(a)

input()

# Answer 1: 162085
# Answer 2: 164123
# Answer 3: 138382