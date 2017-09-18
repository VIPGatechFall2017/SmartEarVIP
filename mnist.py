'''Trains a simple deep NN on the MNIST dataset.

Format: accuracy - seconds/epoch (on Intel Core i5-6300HQ 2.3GHz Quad Core CPU)

DEFAULT
97.8% - 11 s/ep - dense(768,sigmoid)/dropout(0.2)/dense(512,sigmoid)/dropout(0.5)/dense(128,sigmoid)/dense(10,softmax)
CHANGED SECOND TO LAST LAYER TO 256 NEURONS
97.5% - 12 s/ep - dense(768,sigmoid)/dropout(0.2)/dense(512,sigmoid)/dropout(0.5)/dense(256,sigmoid)/dense(10,softmax)
CHANGED ACTIVATION TO RELU ON ALL BUT LAST LAYER
98.3% - 11 s/ep - dense(768,relu)/dropout(0.2)/dense(512,relu)/dropout(0.5)/dense(128,relu)/dense(10,softmax)
HALVED # OF NEURONS & ACTIVATION -> RELU ON ALL BUT LAST LAYER
98.3% -  5 s/ep - dense(384,relu)/dropout(0.2)/dense(256,relu)/dropout(0.5)/dense(64,relu)/dense(10,softmax)
HALVED # OF NEURONS ON ALL BUT LAST LAYER
97.5% -  5 s/ep - dense(384,sigmoid)/dropout(0.2)/dense(256,sigmoid)/dropout(0.5)/dense(64,sigmoid)/dense(10,softmax)
'''

from __future__ import print_function

from numpy.random import seed
seed(1)
from tensorflow import set_random_seed
set_random_seed(2)

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

seed(1)

batch_size = 128
num_classes = 10
epochs = 10

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(384, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
