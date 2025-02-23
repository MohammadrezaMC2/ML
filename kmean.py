from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import k_means, KMeans

x, y = make_blobs(n_samples=300, n_features=2, centers=3)

plt.scatter(x[:,0], x[:, 1],color = 'b')


model = KMeans(n_clusters=3)
model.fit(x)
label = model.labels_
centers = model.cluster_centers_

plt.scatter(x[:,0], x[:,1], c=label)
plt.scatter(centers[:,0], centers[:,1], c='red', marker='x')
plt.show()