import pandas as pd
# import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# Load the data
data = pd.read_csv("Mall_Customers.csv")


X = data.iloc[:, 2:]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


w_css = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    w_css.append(kmeans.inertia_)
    if(i == 10):
        continue

plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), w_css, marker='o', linestyle='--')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('W_CSS')
plt.show()

optimal_clusters = 5


kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)


data['Cluster'] = cluster_labels


print("Cluster Centers:")
print(pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X.columns))


cluster_counts = data['Cluster'].value_counts()
print("\nCluster Counts:")
print(cluster_counts)


plt.figure(figsize=(10, 6))
for cluster in range(optimal_clusters):
    plt.scatter(X_scaled[cluster_labels == cluster, 0],
                X_scaled[cluster_labels == cluster, 1], label=f'Cluster {cluster}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='*', label='Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Scaled Annual Income')
plt.ylabel('Scaled Spending Score')
plt.legend()
plt.show()
