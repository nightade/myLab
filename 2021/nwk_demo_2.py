import numpy as np
import matplotlib.pyplot as plt
import mynetwork as nwk
from scipy.special import factorial as fact

''' CALCULATION SECTION '''
N = 100
p = 0.2    # probability that a node connects to another. (Gilbert Model)
np.random.seed(20210712)

# list of neighbors of the i-th node
src = []
for i in range(N):
    src.append([])
    for j in range(i+1,N):
        if np.random.rand() < p: # ADD LINK
            src[i].append(j)
    for k in range(i):
        if i in src[k]:
            src[i].append(k)

nwk = nwk.create(src)
kvec = nwk.k
kmax, kexp = max(kvec), np.average(kvec)

''' PLOTTING SECTION '''
# LAYOUT
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(13,6), tight_layout=True)

# NODES
pos = np.zeros([N,2])
for i in range(N): # randomly located
    pos[i,0], pos[i,1] = (np.random.rand(), np.random.rand())
ax1.scatter(*pos.T, s=50*kvec, zorder=2, c='tab:green', alpha=0.5)

# LINKS
for p in nwk.get_pair():
    x1, y1 = pos[p[0]]
    x2, y2 = pos[p[1]]
    ax1.plot([x1,x2],[y1,y2], zorder=1, color='lightgrey')

# DEGREES
for i in range(N):
    ax1.annotate(str(kvec[i]), pos[i], fontsize=12)

# k-DISTRIBUTION
kdist, edges = np.histogram(kvec, bins=range(kmax+1), density=True)
ax2.scatter(range(kmax), kdist, color='darkblue')

ax2.plot((kexp, kexp), (0,max(kdist)+0.1), alpha=0.5, lw=3, color='orange', label='<k>')
ax2.plot((0,kmax), (0,0), 'gray', lw=3, alpha=0.3)

poisson = lambda k: np.exp(-kexp) * np.power(kexp,k) / fact(k)
domain = np.linspace(0, kmax, 100)
ax2.fill_between(domain, poisson(domain), alpha=0.3, label='Poisson')

ax2.grid(); ax2.legend(loc='upper right')
plt.show()