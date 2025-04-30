import streamlit as st
import pandas as pd
import io
from  word2number import w2n
import matplotlib.pyplot as plt
import numpy as np

def df_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    return s
    
st.title("The Ecommerce Site")

df = pd.read_csv("ecommerce_customers.csv")

st.write("fetching the dataset", df)
df.columns = df.columns.str.lower().str.replace(" ", "_")

st.write("columns:", df.columns)

df.gender = df.gender.str.strip()
gender_val =  st.text_input("Standadizing the gender Values", placeholder="lower or upper", value="lower").strip()
if gender_val == "":
    st.error('select a gender standardization', icon="🚨")
elif gender_val == "lower":
    df.gender = df.gender.str.lower()
elif gender_val == "upper":
    df.gender = df.gender.str.upper()
else:
    st.error('invalid gender standardization chosen', icon="🚨")

if gender_val in ["lower", "upper"]:
    st.write("Dataframe", df.head())

"summary Information:"
st.text(df_info(df))

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

df_new = df.dropna(ignore_index=True) 

df_new.annual_income = df_new.annual_income.str.lower().str.replace("$", "").str.replace("usd", "").str.strip()

df_new.annual_income = pd.to_numeric(df_new.annual_income)

df_new.last_purchase = pd.to_datetime(df_new.last_purchase,format='mixed' )

df_new.membership_status = df_new.membership_status.str.strip().str.lower()

df_new = df_new.drop_duplicates()

df_new

st.title("Visualizations")

fig, ax = plt.subplots()
ax.hist(df_new.age.values,  histtype='barstacked', )#rwidth=0.8)
ax.set_title("histogram of our ages")
ax.set_xlabel("the various ages")
ax.set_ylabel("thier frequency of occourence")
st.pyplot(fig)


gender_count = {}

for g in df_new.gender.values:
    if gender_count.get(g) == None:
        gender_count[g] = 0
    gender_count[g] += 1

st.write("\n\n\n")
x = gender_count.keys()
y = gender_count.values()
fig, ax = plt.subplots()
ax.bar(x, height=y)
ax.set_title("chart of users according to gender")
st.pyplot(fig)