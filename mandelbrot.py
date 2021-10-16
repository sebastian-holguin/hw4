import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis


def mandelbrot(n, N_max, threshold):
    xmatrix = np.linspace(-2, 1, n)
    ymatrix = np.linspace(-1.5, 1.5, n)
    c = xmatrix[:, newaxis] + 1j * ymatrix[newaxis, :]
    z = 0
    for j in range(N_max):
        z = z**2 + c
    mask = (abs(z) < threshold)
    return mask


mandelbrot_set = mandelbrot(600, 50, 500)

plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')