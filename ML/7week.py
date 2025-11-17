import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram

# 1) 데이터 로드 및 준비
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# 2) 특성 선택 및 스케일링 (꽃받침 길이, 꽃받침 너비)
X_2d = X[:, :2]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_2d)

# 3) K-Means 클러스터링 수행 (k=3)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
clusters_kmeans = kmeans.fit_predict(X_scaled)

# 4) 시각화
plt.figure(figsize=(14, 6))

# --- 실제 품종 분포 산점도 ---
plt.subplot(1, 2, 1)
scatter1 = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title(f"Actual Iris Species Distribution (Features: {feature_names[0]}, {feature_names[1]})")
plt.xlabel("Sepal Length (Scaled)")
plt.ylabel("Sepal Width (Scaled)")
plt.colorbar(scatter1, ticks=[0, 1, 2], label='Actual Species', format=plt.FuncFormatter(lambda val, loc: target_names[val]))

# --- K-Means로 예측한 군집 산점도 ---
plt.subplot(1, 2, 2)
scatter2 = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters_kmeans, cmap='plasma', edgecolor='k', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            marker='X', s=200, c='red', label='Centroids', linewidths=2)
plt.title(f"K-Means Clusters (k={k})")
plt.xlabel("Sepal Length (Scaled)")
plt.ylabel("Sepal Width (Scaled)")
plt.legend()
plt.colorbar(scatter2, ticks=range(k), label='K-Means Cluster ID')

plt.tight_layout()
plt.show()

# 5) 계층적 군집화 (Hierarchical Clustering) 비교 (덴드로그램)
linked = linkage(X_scaled, method='ward')

plt.figure(figsize=(10, 5))
dendrogram(linked, orientation='top')
plt.title("Hierarchical Clustering Dendrogram (Ward Linkage)")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()