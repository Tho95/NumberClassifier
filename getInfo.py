# module to get Information on used Dataset

import tensorflow as tf
import matplotlib.pyplot as plt



def shape(x_train, y_train, x_test, y_test):
    print("x_train: ",x_train.shape)
    print("y_train: ",y_train.shape)
    print("x_test: ",x_test.shape)
    print("y_test: ",y_test.shape)
# We see that an individual input is of the dimension 28x28

#plot the first inputs:
def plot(x_train):
    for i in range(9):
        plt.subplot(330 + 1 + i)
        plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
    plt.show()