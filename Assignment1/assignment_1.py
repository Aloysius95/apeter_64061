# -*- coding: utf-8 -*-
"""Assignment 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IbaVQIp78jN_oyq2PAUbf1uPennQ4NhN

Code given to analyze the KNN and its working
"""

# import modules for this project
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# load iris dataset
iris = datasets.load_iris()
data, labels = iris.data, iris.target

# training testing split
res = train_test_split(data, labels,
                       train_size=0.8,
                       test_size=0.2,
                       random_state=12)
train_data, test_data, train_labels, test_labels = res

# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier
# classifier "out of the box", no parameters
knn = KNeighborsClassifier()
knn.fit(train_data, train_labels)

# print some interested metrics
print("Predictions from the classifier:")
learn_data_predicted = knn.predict(train_data)
print(learn_data_predicted)
print("Target values:")
print(train_labels)
print(accuracy_score(learn_data_predicted, train_labels))

# re-do KNN using some specific parameters.
knn2 = KNeighborsClassifier(algorithm='auto',
                            leaf_size=30,
                            metric='minkowski',
                            p=2,         # p=2 is equivalent to euclidian distance
                            metric_params=None,
                            n_jobs=1,
                            n_neighbors=5,
                            weights='uniform')

knn.fit(train_data, train_labels)
test_data_predicted = knn.predict(test_data)
accuracy_score(test_data_predicted, test_labels)

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

centers = [[2, 4], [6, 6], [1, 9]]
n_classes = len(centers)
data, labels = make_blobs(n_samples=150,
                          centers=np.array(centers),
                          random_state=1)
# do a 80-20 split of the data

# perform a KNN analysis of the simulated data

# output accuracy score

# plot your different results

"""Replicated the study using simulated dataset"""

# Simulated data set provided in the assignment question/reference.
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Define the centers for the blobs
centers = [[2, 4], [6, 6], [1, 9]]
n_classes = len(centers)

# Generate the synthetic dataset
data, labels = make_blobs(n_samples=150,
                          centers=np.array(centers),
                          random_state=1)

# Split the data into training and testing sets
res = train_test_split(data, labels,
                       train_size=0.8,
                       test_size=0.2,
                       random_state=12)
train_data, test_data, train_labels, test_labels = res

# Create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
knn.fit(train_data, train_labels)

# Predict on the training data
learn_data_predicted = knn.predict(train_data)

# Print metrics
print("Predictions from the classifier:")
print(learn_data_predicted)
print("Target values:")
print(train_labels)
print("Accuracy on training data:")
print(accuracy_score(train_labels, learn_data_predicted))

# re-do KNN using some specific parameters.
knn2 = KNeighborsClassifier(algorithm='auto',
                             leaf_size=30,
                             metric='minkowski',
                             p=2,         # p=2 is equivalent to Euclidean distance
                             metric_params=None,
                             n_jobs=1,
                             n_neighbors=5,
                             weights='uniform')

knn2.fit(train_data, train_labels)
test_data_predicted = knn2.predict(test_data)
accuracy_score(test_data_predicted, test_labels)

import matplotlib.pyplot as plt # import the matplotlib library

train_acc_knn = accuracy_score(learn_data_predicted, train_labels)
test_acc_knn2 = accuracy_score(test_data_predicted, test_labels)

# Plotting the results to compare the training and testing accuracy
labels = ['Train Accuracy', 'Test Accuracy']
knn_acc = [train_acc_knn, test_acc_knn2]


x = range(len(labels))

plt.figure(figsize=(8, 5))
plt.bar(x, knn_acc, width=0.4, label='KNN', align='center')


plt.xticks(x, labels)
plt.ylabel('Accuracy')