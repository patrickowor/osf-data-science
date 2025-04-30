#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("ecommerce_customers.csv")


# In[3]:


st.write(df.head())


# In[4]:


#df.index


# In[5]:


df.columns


# In[6]:


df.columns = df.columns.str.lower().str.replace(" ", "_")


# In[7]:


df.columns


# In[8]:


df.gender = df.gender.str.strip().str.lower()
df.head()


# In[9]:


df.info()


# In[17]:


df.age.unique()


# In[22]:


# get_ipython().system('pip install word2number')


# In[26]:


from  word2number import w2n

w2n.word_to_num('twenty-five')


# In[29]:


my_ages = []

for age in df.age.values:
    if pd.isna(age):
        my_ages.append(age) # we plan to fill na with the mean
    else:
        try:
            my_ages.append(int(age))
        except:
            my_ages.append(w2n.word_to_num(age))


# In[31]:


df.age = my_ages
df.info()


# In[32]:


df.head()


# In[36]:


mean = int(df.age.mean())
mean


# In[37]:


df.age.fillna(mean, inplace=True)


# In[38]:


df.info()


# In[54]:


df_new = df.dropna(ignore_index=True) 


# In[55]:


df_new.info()


# In[56]:


df_new.annual_income.unique()


# In[57]:


df_new.annual_income = df_new.annual_income.str.lower().str.replace("$", "").str.replace("usd", "").str.strip()


# In[58]:


df_new.annual_income.unique()


# In[59]:


df_new.annual_income = pd.to_numeric(df_new.annual_income)


# In[60]:


df_new.info()


# In[61]:


df_new.head()


# In[64]:


df_new.last_purchase = pd.to_datetime(df_new.last_purchase,format='mixed' )


# In[65]:


df_new.info()


# In[116]:


df_new.membership_status = df_new.membership_status.str.strip().str.lower()


# In[67]:


df_new = df_new.drop_duplicates()


# In[68]:


df_new.head()


# In[70]:


df_new.info()


# In[ ]:


# visualiztion


# In[81]:


# histtype : {'bar', 'barstacked', 'step', 'stepfilled'}
plt.hist(df_new.age.values,  histtype='barstacked', )#rwidth=0.8)
plt.title("histogram of our ages")
plt.xlabel("the various ages")
plt.ylabel("thier frequency of occourence")
plt.show()


# In[111]:


females = len(list(filter(lambda x:  x, (df_new.gender == "female").values)))


# In[112]:


males = df_new.gender.count() - females
{ 'females': females, 'males': int(males)}


# In[109]:


gender_count = {}

for g in df_new.gender.values:
    if gender_count.get(g) == None:
        gender_count[g] = 0
    gender_count[g] += 1
gender_count


# In[110]:


plt.figure(figsize=(10, 3))

x = gender_count.keys()
y = gender_count.values()
plt.bar(x, height=y)
plt.show()


# In[113]:


df_new.head()


# In[117]:


df_new.membership_status.unique()


# In[118]:


membership_count = {}

for m in df_new.membership_status.values:
    if membership_count.get(m) == None:
        membership_count[m] = 0
    membership_count[m] += 1
membership_count


# In[123]:


plt.figure(figsize=(3, 3))
y = membership_count.values()
labels = membership_count.keys()
explode=[0.1, 0, 0] #optional
plt.pie(y, labels=labels, explode=explode)
plt.show()


# In[127]:


y = df_new.annual_income.values
x = df_new.spending_score.values

plt.scatter(x, y)
plt.xlabel("spending_score")
plt.ylabel("annual_income")
plt.title("annual income vs spending scor")
plt.show()


# In[130]:


df_new.spending_score
df_new.membership_status


# In[135]:


df_new.groupby('gender').count().apply(list)


# In[136]:


spend_grouping = df_new.groupby('membership_status')['spending_score'].apply(list)


# In[139]:


spend_grouping.index


# In[143]:


plt.figure(figsize=(3, 3))
plt.boxplot(spend_grouping, label=list(spend_grouping.index))
plt.show()


# In[144]:





# In[ ]:


st.write('Here is a ecommerce dataset:', df_new)

