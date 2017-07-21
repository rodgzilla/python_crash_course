All the following descriptions are heavily inspired by the "Python
Data Science Handbook" by Jake Vanderplas.

# Supervised models

Supervised learning methods are used to approximate a function for
which we already know some evaluation results. The function could
classify object into classes (classification tasks) or predict a
continuous value (regression tasks).

## Linear Regression

The Linear Regression models are the most basic model used for
regression tasks. They are often used to build a baseline in order to
evaluate more complicated model performances. Such models are popular
because they can be fit very quickly, and are very interpretable.

These models can be extended using a basis function that will derive
more features from the dataset. An example of such basis function is
the PolynomialFeatures class which creates a new features for each
integer exponent value of the data. This can be useful to increase the
complexity of the model and make it work with more complicated data.

The two main regularized versions of Linear Regression are Ridge and
Lasso. These two variants penalize complex models in different
way. Ridge regression penalizes big values in the coefficients of the
model and Lasso allow to select a subset of variables. The subtle
differences between these two algorithms and other variants like
Elastic Net goes beyond the scope of this course, more details can be
found online.

## Naive Bayes

The Naive Bayes models are extremely fast and simple classification
algorithms that are often suitable for very high-dimensional
datasets. Because they are so fast and have so few tunable parameters,
they end up being very useful as a quick-and-dirty baseline for a
classification problem.

Naive Bayes algorithms depend on an assumption on the distribution of
data, for example Gaussian or multinomial.

Because naive Bayesian classifiers make such stringent assumptions
about data, they will generally not perform as well as a more
complicated model. That said, they have several advantages:

- They are extremely fast for both training and predictions
- They provide straightforward probabilistic prediction
- They are often very easily interpretable
- They have very few (if any) tunable parameters

These advantages mean a naive Bayesian classifier is often a good
choice as an initial baseline classification.

Naive Bayes classifiers tend to perform especially well in one of the
following situations:

- When the naive assumptions actually match the data (very rate in
  practice)
- For very well-separated categories, when model complexity is less
  important
- For very high-dimensional data, when model complexity is less
  important

## Support Vector Machines

Support vector machines (SVMs) are a particularly powerful and
flexible class of supervised algorithms for both classification and
regression for the following reasons:

- Their dependence on relatively few support vectors means that they
  are very compact models, and take up very little memory.
- Once the model is trained, the prediction phase is very fast.
- Because they are affected only by points near the margin, they work
  well with high-dimensional data - even data with more dimensions
  than samples, which is a challenging regime for other algorithms.
- Their integration with kernel methods makes them very versatile,
  able to adapt to many types of data.

They have the following disadvantages as well:

- The scaling with the number of samples is O(n^2) which can be
  prohibitive for large numbers of training samples.
- The results are strongly dependent on a suitable choice for the
  softening parameter C. This must be chosen carefully via
  cross-validation, which can be expensive as datasets grow in size.
- The results do not have a direct probabilistic interpretation.

The SVMs are quite tunning intensive. For this reason, it is often a
good idea to use them once simpler and faster models have already been
tried. Using carefully tuned parameters and enough training data, SVMs
can lead to excellent results.

## Decision trees and Random Forests

Random forests are a non-parametric class of ensemble models with
several advantages:

- Both training and prediction are very fast, because of the
  simplicity of the underlying decision trees. In additino both tasks
  can be straightforwardly parallelized, because the individual trees
  are entirely independent entities.
- The multiple trees allow for a probabilistic classification: a
  majority vote among estimators gives an estimate of the probability.
- The nonparametric model is extremely flexible, and can thus perform
  well on tasks that are under-fit by other estimators.

The main disadvantage of random forests is that the results are not
easily interpretable: that is, if you would like to draw conclusions
about the meaning of the classification model, random forests may not
be the best choice.

# Unsupervised models

Unsupervised learning is mostly used to explore the data. Its main
applications are dimensionality reduction, noise filtering, feature
extraction and engineering and clustering.

## Principal component analysis

Principal Component Analysis (PCA) is an algorithm used for
dimensionality reduction. The idea of this algorithm is to build a new
space of lower dimension and project the data points in it in a way
that preserves most of the variance.

PCA can be used for visualization, noise filtering and feature
engineering. A PCA visualization is often a good first step when
working with high dimensional data.

A downside of PCA is that it tends to be highly affected by outliers
in the data. It could be a reason of why PCA is behaving poorly on a
dataset. In this case, other PCA variants that try to mitigate this
problem might be more successful.

## Manifold learning

## k-Means clustering

## Gaussian Mixture Model

## Kernel Density Estimation

