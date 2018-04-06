import matplotlib.pyplot as plt
import numpy as np

plt.figure(dpi=1200)

x = np.linspace(-1,2.5,100000)
y = [max(min(1., s/2.),0.) for s in x] 
plt.plot(x, y,'.')

plt.xlabel('x')
plt.ylabel('P(X<x)')
plt.title('Random number in [0,2]')
plt.grid(True)
plt.xlim(-1,2.5)
plt.ylim(-0.05, 1.05)
plt.savefig("2.png")
plt.show()
