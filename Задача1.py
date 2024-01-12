import numpy as np

n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)] 

d = np.linalg.det(a)

print(d)