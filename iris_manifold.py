import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.manifold import MDS
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.manifold import Isomap

iris    = sns.load_dataset('iris')
X       = iris.drop('species', axis = 1)
y       = iris['species']
classes = list(y.unique())
mds     = MDS(n_components = 2)
lle     = LocallyLinearEmbedding(n_components = 2)
iso     = Isomap(n_components = 2)

X_trans_mds = mds.fit_transform(X)
X_trans_lle = lle.fit_transform(X)
X_trans_iso = iso.fit_transform(X)
colors      = y.apply(classes.index)

fig, ax = plt.subplots(1, 3, figsize = (20, 10))

ax[0].scatter(X_trans_mds[:, 0], X_trans_mds[:, 1], c = colors, cmap = 'rainbow')
ax[0].set_title('Multi dimensional scaling')
ax[1].scatter(X_trans_lle[:, 0], X_trans_lle[:, 1], c = colors, cmap = 'rainbow')
ax[1].set_title('Locally linear embedding')
ax[2].scatter(X_trans_iso[:, 0], X_trans_iso[:, 1], c = colors, cmap = 'rainbow')
ax[2].set_title('Isomap')

plt.show()
