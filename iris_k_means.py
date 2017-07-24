import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster       import KMeans
from sklearn.decomposition import PCA

iris       = sns.load_dataset('iris')
X          = iris.drop('species', axis = 1)
classes_4d = KMeans(n_clusters = 3).fit_predict(X)
pca        = PCA(n_components = 2)
X_trans    = pca.fit_transform(X)
classes_2d = KMeans(n_clusters = 3).fit_predict(X_trans)

fig, ax = plt.subplots(1, 2)

ax[0].scatter(X_trans[:, 0], X_trans[:, 1], c = classes_4d, cmap = 'rainbow')
ax[0].set_title('k-Means on 4D data')
ax[1].scatter(X_trans[:, 0], X_trans[:, 1], c = classes_2d, cmap = 'rainbow')
ax[1].set_title('k-Means on 2D data')
plt.show()
