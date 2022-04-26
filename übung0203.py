import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("IMG_20C.tiff")
npimg = np.array(img, dtype=float)

print("Shape:           ", npimg.shape)
print("Zeilen:          ", npimg.shape[0])
print("Spalten:         ", npimg.shape[1])
print("Farben:          ", npimg.shape[2])
print("nPixel:          ", npimg.shape[0]*npimg.shape[1])
print("First Pixel (RGB)", npimg[0][0])


red = [i for i in range(200)]
green = []
blue = []
for Z in range(npimg.shape[0]):
    for S in range(npimg.shape[1]):
        red.append(npimg[Z][S][0])
        green.append(npimg[Z][S][1])
        blue.append(npimg[Z][S][2])

fig, ax = plt.subplots(nrows=1, ncols=1)
ax.grid(b=True, which='both', color='0.65', linestyle='--')

h = ax.hist(red, bins=256, range=(-0.5, 255.5), histtype="step", color="r")
h = ax.hist(green, bins=256, range=(-0.5, 255.5), histtype="step", color="g")
h = ax.hist(blue, bins=256, range=(-0.5, 255.5), histtype="step", color="b")

plt.show()

def PrintColor(name,color):
    color = np.array(color)
    pix = len(color)
    min = np.amin(color)
    max_ = np.amax(color)
    mean = np.sum(color)/pix
    sigma = 0
    for element in color:
        sigma += (mean-element)**2
    sigma = np.sqrt(sigma/pix)

    print(f"{name}:     Pixel= {pix}       Min= {min}         Max= {max_}          Mean= {mean}        Sigma= {sigma}")


PrintColor("Red", red)
PrintColor("Blue", blue)
PrintColor("Green", green)


