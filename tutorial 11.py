# -*- coding: utf-8 -*-
"""
Created on Thu May 21 07:47:24 2020

@author: rodiyansyah
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans

X = np.random.randint(low = 100, size =(100, 3)) 

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.", "r.", "c.", "y." ]
for i in range(len(X)):
    plt.plot(X[i][0],X[i][1], colors[labels[i]], markersize=10)
plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
plt.show()