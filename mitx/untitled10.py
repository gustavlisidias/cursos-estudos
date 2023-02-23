import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)

plt.figure()

r1 = x - 1
r2 = (12 - 3*x ) / 2
r3 = (3 - 2*x) / 3
r4 = (9 + 2*x) / 3

V = np.array([[2, 1]])
origin = np.array([[0, 0, 0],[0, 0, 0]]) 

plt.plot(x, r1, 'r', label='x-y=1')
plt.plot(x, r2, 'g', label='3x+2y=12')
plt.plot(x, r3, 'y', label='2x+3y=3')
plt.plot(x, r4, 'b', label='-2x+3y=9')

plt.quiver(*origin, V[:,0], V[:,1], color=['m'], scale=21)

plt.legend(loc='upper left')
# plt.axis([0,6,0,6])
plt.grid(True, which='both')
plt.show()
