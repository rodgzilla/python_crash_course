import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.mixture       import GaussianMixture
from sklearn.decomposition import PCA

iris         = sns.load_dataset('iris')
X            = iris.drop('species', axis = 1)
real_classes = iris['species']
classes      = list(real_classes.unique())
real_colors  = real_classes.apply(classes.index)
gmm_4d       = GaussianMixture(n_components = 3).fit(X)
classes_4d   = gmm_4d.predict(X)
pca          = PCA(n_components = 2)
X_trans      = pca.fit_transform(X)
gmm_2d       = GaussianMixture(n_components = 3).fit(X_trans)
classes_2d   = gmm_2d.predict(X_trans)

fig, ax = plt.subplots(1, 3)

ax[0].scatter(X_trans[:, 0], X_trans[:, 1], c = real_colors, cmap = 'rainbow')
ax[0].set_title('Real labels')
ax[1].scatter(X_trans[:, 0], X_trans[:, 1], c = classes_4d, cmap = 'rainbow')
ax[1].set_title('k-Means on 4D data')
ax[2].scatter(X_trans[:, 0], X_trans[:, 1], c = classes_2d, cmap = 'rainbow')
ax[2].set_title('k-Means on 2D data')
plt.show()
