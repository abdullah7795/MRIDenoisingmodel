#!/usr/bin/env python
# coding: utf-8
# git repo-https://github.com/abdullah7795
# In[1]:


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Model
from IPython.display import Image
import imageio
from PIL import Image
from skimage.transform import resize
import os
from os import listdir
import cv2
from PIL import Image
from skimage import color
from skimage import io
import pickle
def preprocess1(array):


    array = array.astype("float32") / 255.0
    array = np.reshape(array, (1, 400, 400,1))
    return array
new_model = tf.keras.models.load_model('my_model')
autoencoder = new_model
img =Image.open('input.tiff').convert('L')
newsize = (400, 400)
img = img.resize(newsize)
np_img1 = np.array(img)
np_img1=preprocess1(np_img1)
predictions2 = autoencoder.predict(np_img1)
for i in predictions2:
    im =i
    i = np.reshape(i, (400, 400))
    imageio.imwrite('outfile5.tif', im)
    plt.imsave("outfile5.tiff", i,cmap='gray')
    
    print("done")





