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

#### Juger les performances d'un modèle

- Validation croisée
- Méthode k-fold

### Feature engineering

#### Variables catégoriques

- Représentation en vecteurs one-hot
- Encodage de valeurs

#### Variables textuelles

- Représentation bag of words
- Word embeddings
- Text embeddings

#### Données manquantes

- Différentes stratégies de gestion des données manquantes
  (suppression, remplacement par la moyenne ou la valeur la plus
  commune, ...)

### Modèles supervisés

#### Régression linéaire

- Concept de régression linéaire
- Régression avec fonction de base (polynomiale, Gaussienne)
- Régularisation (Ridge, Lasso)
- Quand utiliser la régression linéaire

#### Naive Bayes

- Rappel du théorème de Bayes
- Concept de classification générative
- Naive Bayes Gaussien
- Naive Bayes Multinomial
- Quand utiliser Naive Bayes

#### Support Vector Machines

- Concept de classification discriminative
- Maximisation de la marge
- SVM avec kernel
- Quand utiliser les Support Vector Machines

#### Decision trees et Random Forests

- Decision tree
- Concept d'ensemble de model
- Quand utiliser Random Forest

### Modèles non-supervisés

#### Principal component analysis

- Concept de réduction de dimensionalité
- Axes principaux des données
- Quand utiliser la PCA

#### Manifold learning

- Concept de variété non linéaire
- Multidimensional scaling
- Locally linear scaling
- Isometric mapping
- Quand utiliser le Manifold learning

#### k-Means clustering

- Motivation des algorithmes de clustering
- Spectral clustering
- Quand utiliser le k-means clustering

#### Gaussian Mixture Model

- Limitations de PCA
- Modèle d'estimation de densité density estimation
- Quand utiliser les Gaussian Mixture models

#### Kernel Density Estimation

- Utiliser KDE pour représenter graphiquement une distribution de
  points
- Quand utiliser le KDE

### Hyperparameters tuning

- Méthodes de recherche d'hyper paramètres (grid search, random
  search, ...)

# Obtenir les donnees en Python

## Data mining

## Web scraping

- Parsing HTML avec BeautifulSoup

## Connexion à une base de données

- Pourquoi utiliser une base de données ?
- Se connecter à une base de données avec Python

# Big data

## Qu'est-ce que la big data?

- Bases de données relationnelles et scalability
- Systèmes de fichier distribués

## Hadoop avec Python

- Avantages à utiliser du hardware classique
- Système de fichier distribué Hadoop (HDFS, NameNode, DataNode)
- Interface en ligne de commande
- Utilisation de mrjob comme wrapper Hadoop
- MapReduce en Python
- Pig et Python
- Hadoop en Python

## Spark avec Python

- Concept de Spark
- Resilient Distributed Datasets (RDDs)
- Transformations (map, filter, join, ...)
- Actions (reduce, count, first, ...)
- Présentation rapide de Spark Streaming et GraphX

