import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import contingency_matrix
from scipy.stats import entropy
import math


data = pd.read_csv("./dataset/german.csv")

X = data.iloc[:, :2].values  

for n_clusters in (1,2,3,4,5,6,7,8,9,10):
    for max_iter in (100,200,300,400,500):
        kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, random_state=0)
        kmeans.fit(X)

        centro = kmeans.cluster_centers_
        labels = kmeans.labels_

        print(centro)

print("\nCoesão: ",math.sqrt(kmeans.inertia_)/db.n_clusters)
print("\nCoeficiente de Silhueta: ",metrics.silhouette_score(DadosTreino,db.labels_))

for eps in (0.1, 0.2, 0.3, 0.4, 0.5):
    for min_samples in (3, 5, 7, 10):
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        dbscan.fit(X)

        labels = dbscan.labels_

        print("Labels:", labels)


for n_clusters in (2, 3, 4, 5, 6):
    for linkage in ('ward', 'complete', 'average', 'single'):
        agnes = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
        agnes.fit(X)

        labels = agnes.labels_

        print("Labels:", labels)