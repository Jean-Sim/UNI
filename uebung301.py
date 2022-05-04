import matplotlib.pyplot as plt
import math
a = 1
b = 1
lis = [[], []]
for el in range(20):
    a = 1 + 1/(a)
    lis[0].append(a)
    b = math.sqrt(a + 1)
    lis[-1].append(b)

plt.plot(range(20), lis[0], label='Kettenbruch')
plt.plot(range(20), lis[-1], 'r', label='Kettenwurzel')
plt.legend()
plt.show()

# Das Kettenwurzel verfahren Konvergiert schneller