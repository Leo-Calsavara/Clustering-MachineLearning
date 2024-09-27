import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import contingency_matrix
from scipy.stats import entropy
import math


data = pd.read_csv("./dataset/teste.csv")

X = data.iloc[:, :2].values  
y = data['Class'].values
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

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


""" for n_clusters in (1,2,3,4,5,6,7,8,9,10):
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

        print("Labels:", labels) """