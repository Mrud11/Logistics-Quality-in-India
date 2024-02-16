#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd    #1
import numpy as np
import os
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


#load the dataset
data= pd.read_csv(r"D:\Users\Mirdula\Downloads\Leads Report 2021 Numeric Data.csv")
data.head(10)


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


data.isnull().sum()


# In[11]:



# Extract the 'state' and 'quality' columns from the DataFrame
states = data['State wise scores of individual parameters'].tolist()
quality = data['Quality of Road Infrastructure'].tolist()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(states, quality, color='royalblue')
plt.xlabel('State')
plt.ylabel('Quality')
plt.title('Quality by State')

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[12]:


# Extract the 'state' and 'quality' columns from the DataFrame
states = data['State wise scores of individual parameters'].tolist()
quality = data['Quality of Rail Infrastructure'].tolist()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(states, quality, color='royalblue')
plt.xlabel('State')
plt.ylabel('Quality')
plt.title('Quality by State')

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[13]:


# Extract the 'state' and 'quality' columns from the DataFrame
states = data['State wise scores of individual parameters'].tolist()
quality = data['Quality ofWarehousing Infrastructure'].tolist()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(states, quality, color='royalblue')
plt.xlabel('State')
plt.ylabel('Quality')
plt.title('Quality by State')

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[15]:


# Extract the 'state' and 'quality' columns from the DataFrame
states = data['State wise scores of individual parameters'].tolist()
quality = data['Timeliness of Cargo Delivery (Transportation) '].tolist()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(states, quality, color='royalblue')
plt.xlabel('State')
plt.ylabel('Quality')
plt.title('Quality by State')

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[8]:


# Extract the 'state' and 'quality' columns from the DataFrame
states = data['State wise scores of individual parameters'].tolist()
quality = data['Quality of Logistics Services'].tolist()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(states, quality, color='royalblue')
plt.xlabel('State')
plt.ylabel('Quality')
plt.title('Quality by State')

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[9]:


data_score=data['Final Score']
data=data.drop(['Final Score'],axis=1)
sns.scatterplot(x=data_score,y=data['Quality of Logistics Services'])


# In[ ]:




