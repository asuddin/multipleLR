# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EsV6r2sA_MNQ_YiwH6yui5kpmmZNDfJv
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd

data = pd.read_csv("IRIS.csv")
data = data.to_numpy()
#print(data)

X_train = data[:, 1:4]
y_train = data[:, 4]

m = y_train.shape[0]

for i in range(m):
  if y_train[i] == "Iris-setosa":
    y_train[i] = 0
  elif y_train[i] == "Iris-virginica":
    y_train[i] = 1
  else:
    y_train[i] = 2

y_train = y_train.reshape(-1, 1)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units = 25, activation = "sigmoid"),
    tf.keras.layers.Dense(units = 15, activation = "sigmoid"),
    tf.keras.layers.Dense(units = 3, activation = "linear")
])

model.compile(loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
)

X_train1 = np.asarray(X_train).astype(np.float32)
y_train1 = np.asarray(y_train).astype(np.float32)
model.fit(X_train1, y_train1, epochs = 200)

logits = model(X_train1[-1].reshape(1, -1))
modelPrediction = tf.nn.softmax(logits)
print(modelPrediction)