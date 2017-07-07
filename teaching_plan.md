# Introduction to Python

This section starts with an introduction to the Python language and
then introduce the NumPy library, which is used intensively in the
world of data science.

## Basic syntax

### Basic builtin types

- Booleans
- Integers
- Floats
- Strings

### Advanced builtin types

#### Lists

- Definition
- Empty list syntax
- Indexing elements
- Negative indexing
- Appending elements
- Removing elements
- Extending
- Concatenating

#### Tuples

- Definition
- Empty tuple syntax
- Differences with lists

#### Sets

- Definition
- Empty set syntax
- Adding elements
- Removing elements
- Union of sets
- Intersection of sets

#### Dictionaries

- Definitions
- Empty dictionary syntax
- Adding mappings
- Removing mappings

### Loop structures

- For loops
- While loops

### Functions

- Definition
- Parameters
- Default parameters values
- Return
- Basic calls
- Calls using named parameters

### Generators

- Concept
- Call

### Classes

- Quick definition
- Constructor
- Methods

## NumPy

NumPy is an essential tool when manipulating data.

### NumPy array basics

#### Array attributes

- Number of dimensions
- Size of each dimensions
- Total size of the array

#### Indexing

- Positive indices
- Negative indices
- Multi-dimensional indices

#### Slicing

- Slicing syntax
- Multi-dimensional slicing
- No-copy view concept

#### Reshaping

- Reshaping syntax
- Expanding or squeezing axes

#### Concatenating and splitting

- Concatenating syntax
- Stacking syntax
- Splitting syntax
- vsplit, hsplith

### Universal functions

The main reason that NumPy is so efficient is that it provides simple
and optimized way to make computations with arrays of data.

#### Array arithmetic

- Basic arithmetic operations applied on every elements of an array.

#### Aggregates

- Reduce
- Accumulate

### Broadcasting

- Concept
- Examples

### Masking and Boolean Logic

- Masking concept
- Boolean operation on arrays

### Fancy indexing

- Concept of using arrays instead of indices.

## Pandas

Pandas is the other main library to manipulate dataset with
Python. Its role is complementary to NumPy.

### Pandas Objects

- Creation
- Importing from file

### Indexing

- Custom indices
- Slicing using custom indices
- Masking
- Fancy indexing

### Aggregation and Grouping

- Various kind of aggregation (count, mean, std, sum, ...)
- Groupby syntax
- Filtering
- Transforming

## Matplotlib visualization

- Line plots
- Scatter plots
- Histograms

# Machine learning

## What is machine learning?

### Basic concepts

#### Idea of using machine learning to solve problems

- Prediction from data
- Supervised and unsupervised learning
- Classification and regression tasks
- Generalization to unknown data points

#### Judging how a model is doing

- Model cross-validation
- K-fold methods

### Feature engineering

#### Categorical variables

- One hot representation
- Label encoding

#### Text variables

- Bag of words
- Word embeddings
- Text embeddings

#### Missing data

- Different stategies to handle missing data
  (drop, fill with average, fill with most
  common, ...)

### Supervised models

#### Linear Regression

- Concept of linear regression
- Basis function regression (polynomial, Gaussian)
- Regularization (Ridge, Lasso)
- When to use linear regression

#### Naive Bayes

- Bayes theorem.
- Concept of generative classification
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- When to use Naive Bayes

#### Support Vector Machines

- Concept of discriminative classification
- Margin maximization
- Kernel SVM
- When to use Support Vector Machines

#### Decision trees and Random Forests

- Decision trees
- Concept of ensemble models
- When to use Random Forests

### Unsupervised models

#### Principal component analysis

- Concept of dimensionality reduction
- Principal axis of the data
- When to use Principal component analysis

#### Manifold learning

- Concept of non-linear manifolds
- Multidimensional scaling
- Locally linear scaling
- Isometric mapping
- When to use Manifold learning

#### k-Means clustering

- Motivation of clustering algorithms
- Spectral clustering
- When to use k-means clustering

#### Gaussian Mixture Model

- Limitations of PCA
- Density estimation model
- When to use Gaussian Mixture models

#### Kernel Density Estimation


- When to use Kernel Density Estimation

### Hyperparameters tuning

- Hyper parameters search methods (grid search, random search, ...)

# Big data software

## What is big data?

## MapReduce

## Hadoop

## Apache Spark
