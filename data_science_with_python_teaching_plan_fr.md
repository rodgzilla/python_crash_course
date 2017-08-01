# Maths pour le machine learning

Ce chapitre introduit les concepts mathématiques principaux utilisés
en Data Science.

## Algèbre linéare

- Vecteur
- Matrices

## Statistiques

- Tendances
- Corrélations
- Paradoxe de Simpson
- Corrélation and Causalité

## Probability

- Dépendence and Indépendence
- Probabilités conditionnelles
- Théorème de Bayes
- Variables aléatoires
- Distributions
- Test d'hypothèse
- Intervalle de confiance

# Introduction à Python

Ce chapitre commence par une introduction au langage Python et
présente ensuite les principales librairies utilisées en data science.

## Syntaxe de base

### Builtin types basiques

- Booleans
- Integers
- Floats
- Strings

### Builtin types avancés

#### Listes

- Définition
- Syntaxe de liste vidé
- Indéxation des éléments
- Indéxation négative
- Ajout d'éléments
- Suppression d'éléments
- Extension
- Concaténation

#### Tuples

- Définition
- Syntaxe de tuple vide
- Différences avec les listes

#### Sets

- Définition
- Syntaxe d'ensemble vide
- Ajout d'éléments
- Suppression d'éléments
- Union d'ensembles
- Intersection d'ensembles

#### Dictionaries

- Définition
- Syntaxe de dictionnaire vide
- Ajout de correspondance
- Suppression de correspondance

### Structures de boucle

- Boucles for
- Boucles while

### Fonctions

- Définition
- Paramètres
- Valeur par défaut des paramètres
- Return
- Appels classiques
- Appels en utilisant des arguments nommés

### Générateurs

- Concept
- Utilisation

### Classes

- Définition
- Constructeur
- Méthodes

## NumPy

Numpy est un outil essentiel pour la manipulation de données sous
forme matricielle.

### Bases des NumPy array

#### Attributs des array

- Nombre de dimension
- Taille de chaque dimension
- Taille total d'un array
- dtype

#### Indéxation

- Indices positifs
- Indices négatifs
- Indices multi-dimensionnels

#### Slicing

- Syntaxe de slicing
- Slicing multi-dimensionnel
- Concept de vue no-copy

#### Reshaping

- Syntaxe de reshaping
- Expanding et squeezing d'axes

#### Concaténation et splitting

- Syntaxe de concaténation
- Syntaxe de stacking
- Syntaxe de splitting
- vsplit, hsplith

### Fonctions universelles

La principale raison de l'efficacité de Numpy est qu'il fournit des
façons simples et optimisées de faire des calculs sur des matrices de
données.

#### Arithmétique sur des arrays

- Les opérations arithmétique basiques sont appliquées à tous les
  éléments de l'array

#### Aggrégation

- Reduce
- Accumulate

### Broadcasting

- Concept
- Exemples d'utilisation

### Logique booléenne et masking

- Opération booléenne sur les arrays
- Concept de masking

### Indexation fancy

- Concept d'utilisation d'arrays comme indices

## Pandas

Pandas est l'autre principale librairie de manipulation de jeu de
données avec Python. Son rôle est complémentaire à celui de Numpy.

### Objets pandas

- Series
- DataFrame
- Création
- Importation depuis un fichier

### Indéxation

- Indices personnalisés
- Slicing en utilisant les indices personnalisés
- Masking
- Indéxation fancy

### Aggrégation et Grouping

- Plusieurs types d'aggrégation (count, mean, std, sum, ...)
- Syntaxe du Groupby
- Filtrage
- Transformation

## Visualisation avec Matplotlib et Seaborn

- Dessins de courbes
- Dessins de points
- Histogrammes

# Machine learning

## Qu'est-ce que le machine learning?

### Concepts de base

#### Idée d'utiliser le machine learning pour résoudre des problèmes

- Prédictions à partir de données
- Tâches d'apprentissage supervisées et non supervisées
- Tâches de classification et de régression
- Généralisation des modèles à de nouveaux points de données.

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

- Using Kernel Density Estimation to graphically represent a
  distribution of points.
- When to use Kernel Density Estimation

### Hyperparameters tuning

- Hyper parameters search methods (grid search, random search, ...)

# Getting the data with Python

## Data mining

## Web scraping

- BeautifulSoup

## Database connection

- Why do we use databases?
- Database connection with Python

# Big data

## What is big data?

- Relational databases and scalability
- Distributed file systems

## Hadoop with Python

- Advantages of using commodity hardware
- Hadoop distributed file system (HDFS, NameNode, DataNode)
- Command line interface
- mrjob as a Hadoop streaming wrapper
- MapReduce in Python
- Pig and Python
- Hadoop in Python

## Spark with Python

- Spark concept
- Resilient Distributed Datasets (RDDs)
- Transformations (map, filter, join, ...)
- Actions (reduce, count, first, ...)
- Quick presentation of Spark Streaming and GraphX

