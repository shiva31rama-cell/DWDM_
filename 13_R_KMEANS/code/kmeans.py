import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# ============================================================
# STEP 1: Generate sample data
# ============================================================
# Create 300 data points divided into 4 groups.
X, y_true = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=0.60,
    random_state=0
)

# ============================================================
# STEP 2: Setup and train K-Means
# ============================================================
# We use 4 clusters because the sample data has 4 groups.
kmeans = KMeans(
    n_clusters=4,
    init="k-means++",
    random_state=42
)

kmeans.fit(X)

# ============================================================
# STEP 3: Predict cluster for every data point
# ============================================================
y_kmeans = kmeans.predict(X)

# Get the final cluster center points.
centroids = kmeans.cluster_centers_

# ============================================================
# STEP 4: Plot the result
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

# Plot the four cluster centers.
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    s=200,
    marker="X",
    label="Cluster Centers"
)

plt.title("Simple K-Means Clustering Example")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True, linestyle="--", alpha=0.9)
plt.legend()
plt.show()
