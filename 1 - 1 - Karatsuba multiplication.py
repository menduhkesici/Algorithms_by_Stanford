# For Karatsuba multiplication, number of digits of both numbers must be the same

def karatsuba(num_1, num_2):
	len_1 = len(str(num_1))
	len_2 = len(str(num_2))

	if len_1 <= 1:
		return num_1 * num_2

	elif len_2 <= 1:
		return num_1 * num_2

	else:
		i = len_1 // 2
		left_1 = num_1 // 10**i
		right_1 = num_1 % 10**i
		left_2 = num_2 // 10**i
		right_2 = num_2 % 10**i

		a = karatsuba(left_1, left_2)
		b = karatsuba(right_1, right_2)
		c = karatsuba(left_1 + right_1, left_2 + right_2) - a - b
		# in ‘c’, number of digits of the numbers may be different

		return a * 10**(2*i) + c * 10**(i) + b

a = int(input())
b = int(input())

print(karatsuba(a,b))

# Answer: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184