import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE

iris    = sns.load_dataset('iris')
X       = iris.drop('species', axis = 1)
y       = iris['species']
classes = list(y.unique())
tsne    = TSNE(n_components = 2)
X_trans = tsne.fit_transform(X)
colors  = y.apply(classes.index)

plt.scatter(X_trans[:, 0], X_trans[:, 1], c = colors, cmap = 'rainbow')
plt.show()
