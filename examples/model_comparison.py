import numpy             as np
import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble    import RandomForestClassifier
from sklearn.svm         import SVC

iris = sns.load_dataset('iris')
X    = iris.drop('species', axis = 1)
y    = iris['species']

naive_bayes = GaussianNB().fit(X, y)
y_pred_nb   = naive_bayes.predict(X)
errors_nb   = y != y_pred_nb

random_forest = RandomForestClassifier(n_estimators = 50).fit(X, y)
y_pred_rf     = random_forest.predict(X)
errors_rf     = y != y_pred_rf

svc        = SVC().fit(X, y)
y_pred_svc = svc.predict(X)
errors_svc = y != y_pred_svc

print('Error Naive Bayes out of %d: %d' % (X.shape[0], errors_nb.sum()))
print('Error Random Forest out of %d: %d' % (X.shape[0], errors_rf.sum()))
print('Error Support Vector Classifier out of %d: %d' % (X.shape[0], errors_svc.sum()))

iris['result_nb'] = iris['result_rf'] = iris['result_svc'] = iris['species']
iris.loc[errors_nb , 'result_nb'] = 'wrong'
iris.loc[errors_rf , 'result_rf'] = 'wrong'
iris.loc[errors_svc, 'result_svc'] = 'wrong'
plt.title('Naive Bayes')
sns.pairplot(iris, hue='result_nb')
plt.title('Random Forest')
sns.pairplot(iris, hue='result_rf')
plt.title('Support vector classifier')
sns.pairplot(iris, hue='result_svc')

plt.show()
