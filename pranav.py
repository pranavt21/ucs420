#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
data = {
    'calories':[420,380,390],
    'duration':[50,40,45]
}

df=pd.DataFrame(data)
print(df)
print(df.loc==0)


# In[9]:


print(df.iloc[2])


# In[7]:


a=[1,7,2]
myvar=pd.Series(a,index=["x","y","z"])
print(myvar)


# In[14]:


print(df.iloc[:])


# In[13]:


print(df.iloc[0:1])


# In[19]:


print(df.iloc[:,1])


# In[25]:


de=pd.read_csv('iris.csv')
print(de)
print(de.head())


# In[ ]:


de.drop(de.columns[1],axis=1)

