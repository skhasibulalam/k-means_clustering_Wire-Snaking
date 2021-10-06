import math
# import random
import numpy as np
import time
start_time = time.time()
# Function for computing the distance between two co-ords
def distance(x1, y1, x2, y2): 
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)) 

# x = [1, 5, 1.5, 8, 1, 9]
# y = [2, 8, 1.8, 9, 0.6, 11]
x = np.loadtxt('sink.txt', usecols=(1))
y = np.loadtxt('sink.txt', usecols=(2))
k = 5 # Number of Clusters [CHANGE as you wish]

n = len(x)
c = np.zeros((k,2)) # Centroids declared
for i in range (k):
    c[i][0] = x[k-i-1] # Centroids initialized from data
    c[i][1] = y[k-i-1]
temp_c = np.zeros((k,2)) # Temporary Centroids initialized
cluster = np.zeros((k,n,2)) # k-number of Clusters initialized
while ((c!=temp_c).all()):
    temp_c = c.copy()
    jx = 0
    jy = 0
    cstrlen = np.zeros(k) # Length of all Clusters initialized
    dist = np.zeros(k)
    for i in range(n):
        for j in range (k):
            dist[j] = distance(x[i], y[i], c[j][0], c[j][1])
        m = np.argmin(dist)
        g = int(cstrlen[m])
        cluster[m][g][0] = x[i] # Moving to nearest Cluster
        cluster[m][g][1] = y[i]
        cstrlen[m] += 1 # updating the length of that Cluster
    for i in range (k):
        for j in range (int(cstrlen[i])):
            jx += cluster[i][j][0]
            jy += cluster[i][j][1]
        if cstrlen[i]==0 :
            c[i][0] = jx
            c[i][1] = jy
        else :
            c[i][0] = jx / cstrlen[i] #Centroid updating
            c[i][1] = jy / cstrlen[i]
        jx = 0
        jy = 0
d = np.zeros(n) # Distance from Centroids declared
u = 0
for i in range (k):
    for j in range (int(cstrlen[i])):
        d[u] = distance(cluster[i][j][0], cluster[i][j][1], c[i][0], c[i][1])
        u += 1
dmax = 0
for i in range (n):
    if d[i] > dmax :
        dmax = d[i] # dmax updating 
x1 = np.mean(c, axis=0) # Centroid of all centroids
print("--- %.4f seconds ---" % (time.time() - start_time))

import matplotlib.pyplot as plt

plt.plot(x, y, 'ro')
for i in range (k):
    plt.plot(c[i][0],c[i][1],'b*') # Plotting C1,C2,C3,...
plt.plot(x1[0], x1[1], 'gs') # Plotting X1
plt.plot([0,x1[0]], [0,x1[1]]) # O ---> X1
for i in range (k):
    plt.plot([x1[0],c[i][0]], [x1[1],c[i][1]]) # X1--->C1, X1--->C2, X1--->C3,...
u = 0
for i in range (k):
    for j in range (int(cstrlen[i])):
        p = (dmax-d[u])/2
        u += 1
        # C1--->P1, C1--->P2,..., C2--->P5, C2--->P6,...
        plt.plot([c[i][0],c[i][0]+p,cluster[i][j][0]+p,cluster[i][j][0]], [c[i][1],c[i][1],cluster[i][j][1],cluster[i][j][1]])
print("--- %.4f seconds ---" % (time.time() - start_time))
plt.show()
