import numpy as np
import matplotlib.pyplot as plt


# newaxis lets me go up an axis when dealing with the array
# so I don't have to manually change the size depending on n.


def mandelbrot(n, N_max, threshold):
    xmatrix = np.linspace(-2, 1, n)
    # xmatrix uses linspace to create an array of min = -2, max = 1, of n iterations.
    ymatrix = np.linspace(-1.5, 1.5, n)
    # ymatrix uses linspace to create an array of min = -1.5, max = 1.5, of n iterations.
    c = xmatrix[:, np.newaxis] + 1j * ymatrix[np.newaxis, :]
    # getting variables from the start of the matrix, all the way to whatever size
    # our array is. This is the equivalent of getting every index and creating
    # our variable c.
    z = 0
    for i in range(N_max):
        z = z ** 2 + c

    array = (abs(z) < threshold)
    return array


mask = mandelbrot(600, 50, 500)

plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()
plt.savefig('mandelbrot.png')
