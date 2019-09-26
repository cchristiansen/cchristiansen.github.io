import numpy as np

limit = 6000000

fib_0 = np.array([[1],
                  [0]])

A = np.array([[1,1],
              [1,0]])

fib_n = A @ fib_0

stop = 0
i = 0
sum = 1

while stop != 1:
    fib_n = A @ fib_n
    if fib_n[0] > limit:
        stop = 1
    i = i + 1
    if i%3 == 0:
        sum = sum + np.sum(fib_n)

print(sum)
