import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# -----------------------------
# Generate synthetic dataset
# -----------------------------
np.random.seed(42)
normal_data = np.random.normal(0, 1, (1000, 10))
fraud_data = np.random.normal(4, 1, (50, 10))

X = np.vstack([normal_data, fraud_data])
labels = np.array([0]*1000 + [1]*50)

# -----------------------------
# Standardize data
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# PCA Visualization
# -----------------------------
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure()
plt.scatter(X_pca[:,0], X_pca[:,1], c=labels)
plt.title("PCA Visualization")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

# -----------------------------
# t-SNE Visualization
# -----------------------------
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

plt.figure()
plt.scatter(X_tsne[:,0], X_tsne[:,1], c=labels)
plt.title("t-SNE Visualization")
plt.xlabel("Dim1")
plt.ylabel("Dim2")
plt.show()

# -----------------------------
# Isolation Forest (Anomaly Detection)
# -----------------------------
model = IsolationForest(contamination=0.05, random_state=42)
preds = model.fit_predict(X_scaled)

# Convert (-1 anomaly, 1 normal) → (1 anomaly, 0 normal)
anomalies = (preds == -1)

print("Number of detected anomalies:", np.sum(anomalies))

# -----------------------------
# 📊 Graph: Anomaly Detection
# -----------------------------
plt.figure()
plt.scatter(range(len(anomalies)), anomalies)
plt.title("Anomaly Detection (Isolation Forest)")
plt.xlabel("Data Index")
plt.ylabel("Anomaly (1=Yes, 0=No)")
plt.show()