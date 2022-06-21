#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

xnum = np.linspace(-2, 1, 7)
ynum = np.linspace(-1.5, 1.5, 7)
# print (xnum)
# print (ynum)

x,y = np.meshgrid(xnum, ynum)
# print('x = ')
# print(x)
# print('y = ')
# print(y)

print('c = ')
# for a in x:
#     for b in y:
#         c= a + 1j * b
c = x[:] + 1j*y[:]
print(c)


# In[3]:


import numpy as np


N_max = 50

xnum = np.linspace(-2, 1, 7)
ynum = np.linspace(-1.5, 1.5, 7)
# print (xnum)
# print (ynum)

x,y = np.meshgrid(xnum, ynum)

# print('c = ')

c = x[:] + 1j*y[:]
# print(c)

z = c
print('z= ')
for j in range (N_max) :
    z = z**2 + c
    print(z)


# In[4]:


import numpy as np


N_max = 50

xnum = np.linspace(-2, 1, 7)
ynum = np.linspace(-1.5, 1.5, 7)
# print (xnum)
# print (ynum)

x,y = np.meshgrid(xnum, ynum)

# print('c = ')

c = x[:] + 1j*y[:]
# print(c)

z = c
print('mask= ')
for j in range (N_max) :
    z = z**2 + c
#     print(z)
m = np.array(z)

mask = abs(z)< 50
print(mask)


# In[5]:


import numpy as np
import matplotlib.pyplot as plt

N_max = 50

xnum = np.linspace(-2, 1, 7)
ynum = np.linspace(-1.5, 1.5, 7)
# print (xnum)
# print (ynum)

x,y = np.meshgrid(xnum, ynum)

# print('c = ')

c = x[:] + 1j*y[:]
# print(c)

z = c
# print('mask= ')
for j in range (N_max) :
    z = z**2 + c
#     print(z)

m = np.array(z)
mask = abs(z)< 50
# print(mask)

plt.imshow(mask, extent = [-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

def ploting(N_max, threshold, a, b):
    x = np.linspace(-2, 1, a)
    y = np.linspace(-1.5, 1.5, b)

    c = x[:,newaxis] + 1j*y[newaxis,:]
#     print(c)
    z = c 
    for j in range(N_max):
        z = z**2 + c
#           print(z)
        mask = (abs(z) < threshold)

    return mask

mask = ploting(50, 50., 500, 500)

plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')


# In[ ]:




