import matplotlib.pyplot as plt
import numpy as np

plt.figure(dpi=1200)

poss = []
for i in range(6):
    for j in range(6):
        poss.append((i+1,j+1))

x = np.linspace(-1,14,100000)
y = [sum([1 if i+j<s else 0 for i,j in poss])/len(poss) for s in x] 
plt.plot(x, y,'.')

plt.xlabel('x')
plt.ylabel('P(X<x)')
plt.title('Throwing two dices')
plt.grid(True)
plt.xlim(-1,14)
plt.ylim(-0.05, 1.05)
plt.savefig("1.png")
plt.show()
