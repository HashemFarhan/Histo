#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
transfer learning using vgg16
Created on 1/12/2020
Adnan Shdefat
"""

from keras.applications import vgg16
from keras.models import Model
import keras
import pandas as pd
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, InputLayer
from keras.models import Sequential
from keras import optimizers

def vg16(input_shape,Layer_Trainable=[]) :

    vgg = vgg16.VGG16(include_top=False, weights='imagenet',input_shape=Layer_Trainable)

    output = vgg.layers[-1].output
    output = keras.layers.Flatten()(output)
    vgg_model = Model(vgg.input, output)

    set_trainable = False
    for layer in vgg_model.layers:
        if layer.name in true:
            set_trainable = True
        if set_trainable:
            layer.trainable = True
        else:
            layer.trainable = False

    layers = [(layer, layer.name, layer.trainable) for layer in vgg_model.layers]
    y =pd.DataFrame(layers, columns=['Layer Type', 'Layer Name', 'Layer Trainable'])  
    return (y)
                        

    
    
def add3layer (L1nodes, L1activation ,L2nodes, L2activation ,L3nodes, L3activation):  

    model = Sequential()
    model.add(vgg_model)
    model.add(Dense(L1nodes, activation=L1activation, input_dim=input_shape))
    model.add(Dropout(0.3))
    model.add(Dense(L2nodes, activation=L2activation))
    model.add(Dropout(0.3))
    model.add(Dense(L3nodes, activation=L3activation))


def compilevgg (loss , optimizer, metrics):
    model.compile(loss=loss,
              optimizer=optimizer,
              metrics=metrics)
    return model.summary() 


def modelfit (train_data,steps_per_epoch,epochs,validation_data,validation_steps):
    
    history = model.fit_generator(train_data, steps_per_epoch=steps_per_epoch, epochs=epochs,
                              validation_data=validation_data, validation_steps=validation_steps, 
                              verbose=1)    
    return history
    


# In[ ]:




