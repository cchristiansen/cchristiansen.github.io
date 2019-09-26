a = 0
b = 1
sum = 0
while b < 6000000:
	x = a+b
	a = b
	b = x
	if b%2 == 1:
		sum = sum + b
print(sum)	
