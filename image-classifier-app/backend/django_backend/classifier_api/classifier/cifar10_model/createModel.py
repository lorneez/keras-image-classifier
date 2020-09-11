# Imports:
# keras: python neural network library
# Sequential: stacks layers in a model
# Dense: layer that is densely connected
# Dropout: layer that drops % of nodes
# Flatten: layer that flattens input to 1D
# Conv2D: layer that performs 2D convolution
# MaxPooling2D: layer that performs 2D max pooling to reduce size
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

def createModel():
    # Create sequential model
    model = Sequential()
    # Add two Conv2D layers
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32,32,3)))
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
    # Add MaxPooling2D layer
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Add dropout layer 25%
    model.add(Dropout(0.25))
    # Add two Conv2D layers
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    # Add MaxPooling2D layer
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Add dropout layer 25%
    model.add(Dropout(0.25))
    # Add flatten layer
    model.add(Flatten())
    # Add dense layer
    model.add(Dense(512, activation='relu'))
    # Add dropout layer 50%
    model.add(Dropout(0.5))
    # Add dense layer
    model.add(Dense(10, activation='softmax'))

    model.load_weights('classifier/cifar10_model/cifar_weights_2.h5')

    # Compile model using loss: categorical_crossentropy, optimizer: adam
    model.compile(loss='categorical_crossentropy',
         optimizer='adam',
         metrics=['accuracy'])

    return model
