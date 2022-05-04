a = open('Higgs.txt', 'r+')
b = list(a.read())
c = open('Higgs2.txt', 'r+')
d = list(c.read())

import matplotlib.pyplot as plt


def deocde(word):
    key =   list("ABCDEFGHIJKNMLOPQRSTUVWXYZ")
    Alpha = word

    for char in range(len(d)):
        for dot in range(len(Alpha)):
            if Alpha[dot] == d[char].upper():
                d[char] = key[dot]
                break

def count(lis):
    count = [0 for i in range(26)]
    print(count)
    for el in range(len(lis)):
        for num in range(26):
            if lis[el].upper() == "ABCDEFGHIJKNMLOPQRSTUVWXYZ"[num]:
                count[num] += 1
    return count


plt.plot(range(26), count(b), 'b+', label='vorher')
plt.plot(range(26), count(d), 'r+', label='nachher')
plt.xlabel('Buchstaben Index')
plt.ylabel('Anzahl')
plt.legend
plt.show()


deocde("test")
print(''.join(d))
a.close()