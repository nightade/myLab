import numpy as np
import matplotlib.pyplot as plt
import mynetwork as nwk

test = [[1,2,3], [0,2,4], [0,1], [0,4], [1,3]]

testnwk = nwk.create(test)
print('Nodes :', testnwk.N)
print('k-sequence :', testnwk.k)
print('\'src\' = ', testnwk.src)

N = testnwk.N
src = testnwk.src
kvec = testnwk. k

arrPair = testnwk.get_pair()
L = testnwk.get_L()

pos = np.zeros([N,2])
for i in range(N):
    pos[i,0] = np.random.rand()
    pos[i,1] = np.random.rand()

fig_demo, ax_demo = plt.subplots(1)
ax_demo.scatter(*pos.T, s=300, c='hotpink', zorder=2)

arrLine = []
for i in range(L):
    x1 = pos[arrPair[i,0], 0]
    y1 = pos[arrPair[i,0], 1]
    x2 = pos[arrPair[i,1], 0]
    y2 = pos[arrPair[i,1], 1]
    newline = ax_demo.plot([x1,x2],[y1,y2], zorder=1, color='grey')
    arrLine.append(newline)
    
# DEGREES
for i in range(N):
    ax_demo.annotate(str(i), pos[i]+(-0.0074, -0.011), fontsize=14)
    
plt.show()