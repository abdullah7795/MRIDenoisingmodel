#!/usr/bin/env python
# coding: utf-8

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

import os
from os import listdir
import cv2


from skimage import color
from skimage import io


# In[2]:


import pickle

def preprocess1(array):


    array = array.astype("float32") / 255.0
    array = np.reshape(array, (1, 400, 400,1))
    return array

# In[6]:


new_model = tf.keras.models.load_model('my_model')
autoencoder = new_model


# In[12]:


img =cv2.imread('input.tiff',0)

np_img1 = np.array(img)
print(np_img1.shape)
print(np_img1.shape)
np_img1=preprocess1(np_img1)

print(np_img1.shape)


# In[8]:




# In[13]:


predictions2 = autoencoder.predict(np_img1)


# In[14]:


n = 1
f = plt.figure(figsize=(400, 400))
y=0
for i in predictions2:
        # Debug, plot figure
    y=y+1
    f.add_subplot(10, 10, y)
    plt.gray()
    plt.imshow(i)

plt.show(block=True)


# In[15]:





for i in predictions2:
    im =i
    i = np.reshape(i, (400, 400))
    imageio.imwrite('Denoised_Output_Image.tif', im)
    plt.imsave("Denoised_Output_Image.tiff", i,cmap='gray')
    
    print(im.shape)


# In[ ]:




