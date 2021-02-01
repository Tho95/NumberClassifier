# program for classifing numbers (MNIST Handwritten Digit Classification Dataset)

import numpy as np
import keras
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd

import getInfo
import ignoreGreyscale
import create_model
import test_model

#load data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
#normalize train_data to have values between [0,1]
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

getInfo.shape(x_train, y_train, x_test, y_test)

getInfo.plot(x_train)

x_train = ignoreGreyscale.toBlack(x_train)

create_model.first_model(x_train,y_train)

x_test = ignoreGreyscale.toBlack(x_test)

test_model.evaluate(x_test,y_test)

