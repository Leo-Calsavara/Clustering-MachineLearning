import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import contingency_matrix
from scipy.stats import entropy
import math
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics


data = pd.read_csv("./dataset/teste.csv")

X = data.iloc[:, :2].values  
y = data['Class'].values

# Suponha que X são os dados originais (sem redução de dimensionalidade)
# E y são as classes, onde 1 = Good e 2 = Bad

# Reduzindo para 2 dimensões com PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)  # Reduz para 2 dimensões

# Visualizando as classes reais (Good/Bad)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, palette={1: 'green', 2: 'red'}, s=100)  # 1=Good, 2=Bad
plt.title('Classes Reais (Good/Bad)')
plt.savefig('classes_reais.png')  # Salva a figura como um arquivo PNG
plt.close()

best = -1
best_i = 0
best_j = 0

for n_clusters in (1,2,3,4,5,6):
    for max_iter in (200,300,400):
        kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, random_state=0)
        kmeans.fit(X)

        Completude = metrics.completeness_score(y,kmeans.labels_)

        if(Completude > best):
            best_i = n_clusters
            best_j = max_iter

kmeans = KMeans(n_clusters=best_i, max_iter=best_j, random_state=0)
kmeans.fit(X)

print("\nSoma dos quadrados das distâncias até o centróide mais próximo: ",kmeans.inertia_)

print("\nCoesão: ", math.sqrt(kmeans.inertia_)/kmeans.n_clusters)

print("\nCoeficiente de Silhueta: ",metrics.silhouette_score(X,kmeans.labels_))

print("\nRand Score K-means: ",metrics.rand_score(y,kmeans.labels_))

print("\nHomogeneidade : ",metrics.homogeneity_score(y,kmeans.labels_))

print("\nCompletude : ",metrics.completeness_score(y,kmeans.labels_))


best = -1
best
for eps in (0.1, 0.2, 0.3, 0.4, 0.5):
    for min_samples in (3, 5, 7, 10):
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        dbscan.fit(X)

        labels = dbscan.labels_



for n_clusters in (2, 3, 4, 5, 6):
    for linkage in ('ward', 'complete', 'average', 'single'):
        agnes = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
        agnes.fit(X)

        labels = agnes.labels_

