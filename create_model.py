# module for crating and trying different models which can be called as functions

import keras
import tensorflow as tf

def first_model(x_train,y_train):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())     # flatten for neural network (dense expects 1 dimension input)
    model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

    model.compile(optimizer ='adam',
                  loss = 'sparse_categorical_crossentropy',
                  metrics =['accuracy'])
    model.fit(x_train, y_train, epochs = 3)
    model.save('numberIdentification')