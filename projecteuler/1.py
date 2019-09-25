i = 0
sum = 0
while i < 1000:
    if i%5 == 0 or i%7 == 0 or i%11 == 0: 
        sum = sum + i
    i = i+1
print sum
