import numpy as np
import matplotlib.pyplot as plt

# Class for arbitrary UNDIRECTED network
# src : ndarray not allowed (inhomogenous seq.)
class Network:
    def __init__(self, src):
        self.src = src
        self.N = len(src)
        self.k = np.zeros(self.N, dtype=int)
        for i in range(self.N):
            self.k[i] = len(src[i])
    
    def rmv_node(self, target):
        neighbor = self.src[target]
        for n in neighbor:
            self.src[n].pop(target)
            self.k[n] -= 1
        self.src.pop(target)
        self.k = np.delete(self.k, target)
        self.N -= 1
        return True
    
    def add_node(self, neighbor):
        for n in neighbor:
            self.src[n].append(self.N)
            self.k[n] += 1
        self.src.append(neighbor)
        self.k = np.append(self.k, len(neighbor))
        self.N += 1
        return True
    
    def rmv_link(self, a, b):
        self.src[a].remove(b)
        self.src[b].remove(b)
        self.k[a] -= 1
        self.k[b] -= 1
        return True
    
    def add_link(self, a, b):
        self.src[a].append(b)
        self.src[b].append(a)
        self.k[a] += 1
        self.k[b] += 1
        return True
    
    def get_pair(self):
        pairs = []
        for i in range(self.N):
            for j in range(self.k[i]):
                if i < self.src[i][j]:
                    pairs.append([i, self.src[i][j]])
        return np.array(pairs)
    
    def get_L(self):
        return len(self.get_pair())
        

def create(src):
    return Network(src)