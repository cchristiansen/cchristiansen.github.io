import numpy as np
import itertools

def triangular(a,b):
    n = (b-1)/a
    return a*n*(n+1)/2

def addon(i, vtriangular, nums, limit):
    return((-1)**(i%2)*vtriangular(list(np.prod(x) for x in list(itertools.combinations(nums,i+1))),limit))

limit = 1000
nums = [5,7,11]

vtriangular = np.vectorize(triangular)

print(sum(list(sum(addon(i,vtriangular,nums,limit)) for i in range(len(nums)))))
