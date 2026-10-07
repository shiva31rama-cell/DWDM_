# LIBRARIES USED
# matplotlib.pyplot -> draws the final cluster graph.
# numpy             -> provides numerical array support.
# sklearn.cluster.KMeans -> provides the K-Means algorithm.
# sklearn.datasets.make_blobs -> creates sample grouped data.
#
# DATASET
# X contains 400 generated numerical points divided into four groups.
# y_true stores the original generated group labels for reference.
#
# HOW IT WORKS
# 1. Generate sample data.
# 2. Create the K-Means model.
# 3. Train the model.
# 4. Predict the cluster of each point.
# 5. Get the cluster centers.
# 6. Plot the points and centers.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# ============================================================
# STEP 1: Generate sample dummy data
# ============================================================
# The data contains 400 points divided into 4 groups.
X, y_true = make_blobs(
    n_samples=400,
    centers=4,
    cluster_std=0.60,
    random_state=0
)

# ============================================================
# STEP 2: Setup and train the K-Means algorithm
# ============================================================
kmeans = KMeans(
    n_clusters=4,
    init="k-means++",
    random_state=42
)

kmeans.fit(X)

# ============================================================
# STEP 3: Predict groups and get centroids
# ============================================================
y_kmeans = kmeans.predict(X)
centroids = kmeans.cluster_centers_

# ============================================================
# STEP 4: Plot the visual result
# ============================================================
plt.figure(figsize=(9, 7))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y_kmeans,
    s=50,
    cmap="viridis",
    alpha=0.9,
    label="Data Points"
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    s=200,
    marker="X",
    label="Cluster Centers"
)

plt.title("Simple K-Means Clustering Result")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True, linestyle="--", alpha=0.9)
plt.legend()
plt.show()
