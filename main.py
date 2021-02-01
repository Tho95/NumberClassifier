# program for classifing numbers (MNIST Handwritten Digit Classification Dataset)

import numpy as np
import keras
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd

import getInfo
import ignoreGreyscale
#load data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
#normalize train_data to have values between [0,1]
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_train = tf.keras.utils.normalize(x_train, axis=1)

getInfo.shape(x_train, y_train, x_test, y_test)

getInfo.plot(x_train)

x_train = ignoreGreyscale.toBlack(x_train)



