import numpy as np

A = np.array(range(10))

for i in range(5):
    print(A[i])

print('---------')

for i in range(5):
    print(A[i*2])

print('---------')

print(A[-1])

print('---------')

for i in range(1, 6):
    print(A[-i])

print('---------')

for i in range(len(A)-2):
    print(A[i])

print('---------')

for i in range(1,11):
    print(A[-i])

print('---------')

for i in range(3):
    print(A[2-i])

print('---------')

for i in range(1, 3):
    print(A[-i])

print('---------')

for i in range(3, 11):
    print(A[-i])

