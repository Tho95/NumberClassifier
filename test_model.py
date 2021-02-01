# module for testing a model with the test_data

import tensorflow as tf
import keras
import matplotlib.pyplot as plt

def evaluate(x_test, y_test):
    model =tf.keras.models.load_model('first_model.model')

    print('model loaded')
    model.evaluate(x_test, y_test)
    print('model evaluation complete')

def plot(history):
    plt.plot(history.history['acc'])
    plt.plot((history.history['val_acc']))
    plt.title('model accuracy')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(['train', 'val'],loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot((history.history['val_loss']))
    plt.title('model loss')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()