import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, adjusted_rand_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.decomposition import PCA

iris_data = pd.read_csv('C:/Users/user/Downloads/iris_cluster.csv')

# making dataset with columns
iris_df = pd.DataFrame(iris_data)
iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
true_labels = iris_df['class'] # true class labels
dropped_iris_df = iris_df.drop(columns=['class'])
# print(iris_df)

# preprocessing data
scaler = StandardScaler() # normalize numerical features
adjusted_iris = scaler.fit_transform(dropped_iris_df)
# print(adjusted_iris)

# K-Means Clustering
inertia = []
K_range = range(1, 11)
for k in K_range:
    k_means = KMeans(n_clusters=k, random_state=42, n_init=10)
    k_means.fit(adjusted_iris)
    inertia.append(k_means.inertia_)

# elbow method
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.show()

# Fit K-means clustering to data
k_meaning = KMeans(n_clusters=3, random_state=24, n_init=10)
k_meaning_labels = k_meaning.fit_predict(adjusted_iris)

# Hierarchical Clustering
linked_matrix = linkage(adjusted_iris, method='ward')
plt.figure(figsize=(10,5 ))
dendrogram(linked_matrix)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

# Fit Hierarchical Clustering to data
hierarchy = AgglomerativeClustering(n_clusters=3)
hierarchy_labels = hierarchy.fit_predict(adjusted_iris)

# Evaluation Metrics (Silhouette Score, Adjusted Rand Index)
k_means_silhouette = silhouette_score(adjusted_iris, k_meaning_labels)
hierarchy_silhouette = silhouette_score(adjusted_iris, hierarchy_labels)

k_means_ari = adjusted_rand_score(true_labels, k_meaning_labels)
hierarchy_ari = adjusted_rand_score(true_labels, hierarchy_labels)

print(f"Silhouette Score (K-Means): {k_means_silhouette:.2f}")
print(f"Silhouette Score (Hierarchical): {hierarchy_silhouette:.2f}")
print(f"Adjusted Rand Index: (K-Means): {k_means_ari:.2f}")
print(f"Adjusted Rand Index: (Hierarchical): {hierarchy_ari:.2f}")

# Reduce dimensions using PCA for visualization
pca = PCA(n_components=2)
iris_pca = pca.fit_transform(adjusted_iris)

# Plot clusters 
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(iris_pca[:, 0], iris_pca[:, 1], c=k_meaning_labels, cmap='viridis')
axes[0].set_title('K-Means Clustering')
axes[1].scatter(iris_pca[:, 0], iris_pca[:, 1], c=hierarchy_labels, cmap='viridis')
axes[1].set_title('Hierarchical Clustering')
plt.show()