x = 600851475147

def largestprimefactor(x):
    for i in range(2,int(x**0.5)+1,1):
        if x%i == 0:
            return largestprimefactor(x/i)
    return x

print(largestprimefactor(x))
