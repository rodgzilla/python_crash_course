# Neural networks

## Neurons

- Inputs / output
- Weights
- Bias
- Activation function
- Neuron computation as matrix multiplications

## Neuron Layers

- Neural network: set of connected neurons
- Concept of layers
- Input, hidden and output layers

## Example networks: logical gate

- AND gate
- OR gate
- (maybe) XOR gate

# Training algorithms

## Gradient descent

- Concept of using the derivative to find a local minima of a function
- Example of linear regression
- Concept of backpropagation

## Learning rate

- Concept of learning rate
- Automatic learning rate tuning via cyclical learning rate

## Convolution layers

- Definition of convolution
- Examples of convolution (Sobel operators, ...)
- Convolutions are a way to focus the network computations on spatial
  informations
- Explanation of how convolution kernels are modified by gradient
  descent

# Practical deep learning

## Using pre-trained networks

### Available pre-trained networks

- Why use pre-trained networks (training data, computation power
  required for training, ...)
- Quick list of popular available networks
- Example of using a VGG16 neural network (trained with the imagenet
  dataset) to classify pictures

### Transfer learning

- Concept of finetuning
- Finetuning in practice (Intuition on the number of layers to
  retrain, etc.)
- Finetuning of a VGG16 network to compete in the Cats vs Dogs Kaggle
  competition

## Working with images

- Image classification
- Object detection
- Image segmentation
- (Maybe) Image generation (GAN concept + quick MNIST example)

## Natural language processing

- Concept of word embeddings
- Available pre-trained word embeddings
- Application to text classification
- Quick intro on recurrent and attention models

## Recommender system

- Transfering the concept of word embeddings to users and products
- Building a recommender system on the MovieLens dataset.

## Time series

- Introduction on time series workflow with neural networks.
