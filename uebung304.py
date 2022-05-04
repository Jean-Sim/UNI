import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt('Raw Data.csv', delimiter=',', skip_header=1)
data2 = np.genfromtxt('Raw Data2.csv', delimiter=',', skip_header=1)
data3 = np.genfromtxt('Raw Data3.csv', delimiter=',', skip_header=1)

time1 = data1[:, 0]
time2 = data2[:, 0]
time3 = data3[:, 0]

A1 = data1[:,3]
A2 = data2[:,2]
A3 = data3[:,1]

plt.hist(A1)
plt.hist(A2)
plt.hist(A3)
plt.show()

mittel = [np.mean(A1), np.mean(A2), np.mean(A3)]
st_abw = [np.std(A1), np.std(A2), np.std(A3)]
print(f"Mittelwerte: {mittel}")
print(f"Standartabweichung: {st_abw}")

fig1, ax1 = plt.subplots()
ax1.errorbar(time1, A1, yerr=st_abw[0], label="1")
fig2, ax2 = plt.subplots()
ax2.errorbar(time2, A2, yerr=st_abw[1], label="2")
fig3, ax3 = plt.subplots()
ax3.errorbar(time3, A3, yerr=st_abw[2], label="3")
plt.legend
plt.show()