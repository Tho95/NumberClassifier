# module for testing a model with the test_data

import tensorflow as tf
import keras
def evaluate(x_test, y_test):
    model =tf.keras.models.load_model('numberIdentification.model')
    print('model loaded')
    model.evaluate(x_test,y_test)
    print('model evaluation complete')