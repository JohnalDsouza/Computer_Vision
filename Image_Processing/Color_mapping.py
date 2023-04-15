#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import matplotlib.pyplot as plt


# In[9]:


img = cv2.imread('00-puppy.jpg')


# In[10]:


type(img)


# In[11]:


plt.imshow(img)


# In[12]:


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)


# In[13]:


img =  cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
plt.imshow(img)


# In[15]:


img =  cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
plt.imshow(img)


# In[ ]:




