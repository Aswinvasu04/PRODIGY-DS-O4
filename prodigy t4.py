#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install textblob


# In[9]:


import pandas as pd 
import numpy as np 
from textblob import TextBlob
import matplotlib.pyplot as plt 


# In[10]:


data=pd.read_csv("twitter_training.csv")


# In[11]:


col_names = ['ID', 'Entity', 'Sentiment', 'Content']
df = pd.read_csv('twitter_training.csv', names=col_names)


# In[12]:


df.head()


# In[13]:


df.tail()


# In[14]:


df.shape


# In[15]:


df.describe


# In[16]:


df.isnull().sum()


# In[17]:


df.dropna(axis=0 , inplace=True)
df.isnull().sum()
     


# In[18]:


sentiment_counts = df['Sentiment'].value_counts()
sentiment_counts
     


# In[21]:


brand_data = df[df['Entity'].str.contains('Microsoft', case=False)]
brand_sentiment_counts = brand_data['Sentiment'].value_counts()
brand_sentiment_counts 


# In[22]:


plt.figure(figsize=(6, 6))
plt.pie(brand_sentiment_counts, labels=brand_sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Distribution for Microsoft')
plt.show()


# In[26]:


plt.figure(figsize=(6, 3))
sentiment_counts.plot(kind='bar', color=['black', 'red', 'pink', 'blue'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=0)
plt.show()


# In[ ]:




