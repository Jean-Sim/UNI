a = open('Higgs.txt', 'r+')
b = list(a.read())

def encode():
    key = list("TYRANOPFEXBIDUCVWZMQSJKLGH")
    Alpha=list("ABCDEFGHIJKNMLOPQRSTUVWXYZ")
    print(len(Alpha))

    for char in range(len(b)):
        for dot in range(len(Alpha)):
            if Alpha[dot] == b[char].upper():
                b[char] = key[dot]
                break

def deocde(word):
    key =   list("ABCDEFGHIJKNMLOPQRSTUVWXYZ")
    Alpha = word

    for char in range(len(b)):
        for dot in range(len(Alpha)):
            if Alpha[dot] == b[char].upper():
                b[char] = key[dot]
                break



encode()
print(''.join(b))
c = open('Higgs2.txt', 'w')
c.write(''.join(b))
a.close()
