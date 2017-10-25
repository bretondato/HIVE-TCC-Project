import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import SOM_TNSRFLW as som
from collections import Counter



"""
plt.figure(figsize=(12, 12))

n_samples = 2000
random_state = 170
X, y = make_blobs(n_samples=n_samples, n_features=300, random_state=random_state)

print(X)
print(y)

# Incorrect number of clusters
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Incorrect Number of Blobs")
plt.show()

"""
dt = []
set = []
f = open('Dataset_exemple_Tree_Cluster', 'r')

for i in f:
    dt.append(f.readline().split())
    #set.append(dt)
    #dt = []

print(dt)




som = som.SOM(2, 4, 2, 100)
som.train(dt)

image_grid = som.get_centroids()

mapped = som.map_vects(dt)
print(mapped)
print(len(mapped))
print(len(dt))

fr = []

for i, m in enumerate(mapped):
    fr.append(m)
    count = Counter(map(tuple, fr))
    count = dict(count)

print(count)

for i, m in enumerate(dt):
    #print(som_in[i][1])
    plt.plot(dt[i][1], dt[i][0], 'ro')
#plt.plot(som_in, 'ro')
plt.show()
