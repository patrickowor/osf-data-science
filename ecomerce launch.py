import streamlit as st
from  word2number import w2n

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("cleaning/ecommerce_customers.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_")

df.gender = df.gender.str.strip().str.lower()

my_ages = []

for age in df.age.values:
    if pd.isna(age):
        my_ages.append(age) # we plan to fill na with the mean
    else:
        try:
            my_ages.append(int(age))
        except:
            my_ages.append(w2n.word_to_num(age))
df.age = my_ages
mean = int(df.age.mean())
df.age.fillna(mean, inplace=True)
df_new = df.dropna(ignore_index=True) 
df_new.annual_income = df_new.annual_income.str.lower().str.replace("$", "").str.replace("usd", "").str.strip()

df_new.annual_income = pd.to_numeric(df_new.annual_income)

df_new.last_purchase = pd.to_datetime(df_new.last_purchase,format='mixed' )

df_new.membership_status = df_new.membership_status.str.strip().str.lower()

df_new = df_new.drop_duplicates()
st.title("E - commerce Report")
st.write('Here is a our dataset:', df_new)