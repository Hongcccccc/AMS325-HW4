#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
n=5
tmp = np.random.rand(n,1)
p = tmp/tmp.sum()
print(p)


# In[ ]:


tmp = np.random.rand(n,n)
P = tmp/tmp.sum(axis=1,keepdims=1)
print(P)


# In[ ]:


p_old = p
N=500
for i in range(N):
    p_old=np.dot(P.transpose(),p_old)

print(p_old)


# In[ ]:


pp = np.linalg.eig(P.transpose())
eigenV=pp[1]
eigenVL=pp[0]
# print("eigenV")
# print(eigenV)
# print("eigenVL")
# print(eigenVL)
tmp=eigenV[:,np.argmax(eigenVL)]
p_stationary=tmp/tmp.sum()
print("p_stationary")
print(p_stationary)


# In[ ]:


p_old = p
# N=5
N=50
# N=500
for i in range(N):
    p_old=np.dot(P.transpose(),p_old)
    
print(np.linalg.norm(p_old.transpose()-p_stationary)/np.linalg.norm(p_stationary))


# In[ ]:


def test(n,N):
    import numpy as np

    tmp = np.random.rand(n,1)
    p = tmp/tmp.sum()
    tmp2 = np.random.rand(n,n)
    P = tmp2/tmp2.sum(axis=1,keepdims=1)
    p_old = p
    for i in range(N):
        p_old=np.dot(P.transpose(),p_old)
        
    return p_old
print(test(5,50))
print(test(10,600))

