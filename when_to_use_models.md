All the following descriptions are inspired by the "Python Data
Science Handbook" by Jake Vanderplas.

# Supervised models

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


## Decision trees and Random Forests


# Unsupervised models

## Principal component analysis


## Manifold learning

## k-Means clustering

## Gaussian Mixture Model

## Kernel Density Estimation

