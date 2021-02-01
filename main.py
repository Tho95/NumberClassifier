# program for classifing numbers (MNIST Handwritten Digit Classification Dataset)

import numpy as np
import keras
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd

import getInfo

#load data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

getInfo.shape(x_train, y_train, x_test, y_test)

getInfo.plot(x_train)



