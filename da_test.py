import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import streamlit as st

st.title("Imperial Healthtech Customer Activity Dashboard")
st.write("Muhamad Bagus Septian")

df = pd.read_csv("app_data.csv")

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_data(df):
    df = pd.read_csv("app_data.csv")
    return df

data = copy.deepcopy(load_data(df))

data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

sns.set()
st.subheader("Daily Device Installs in November 20222")
fig1, ax1 = plt.subplots(figsize=(20,5))
sns.lineplot(x=data["Date"], data=data, y=data["Daily Device Installs"])
st.pyplot(fig1)

st.subheader("Daily User Installs in November 20222")
fig2, ax2 = plt.subplots(figsize=(20,5))
sns.lineplot(x=data["Date"], data=data, y=data["Daily User Installs"])
sns.set()
st.pyplot(fig2)

st.subheader("Daily User Uninstalls in November 20222")
fig3, ax3 = plt.subplots(figsize=(20,5))
sns.lineplot(x=data["Date"], data=data, y=data["Daily User Uninstalls"])
sns.set()
st.pyplot(fig3)

st.subheader("Active Device Installs in November 20222")
fig4, ax4 = plt.subplots(figsize=(20,5))
sns.lineplot(x=data["Date"], data=data, y=data["Active Device Installs"])
sns.set()
st.pyplot(fig4)

st.subheader("Install events in November 20222")
fig5, ax5 = plt.subplots(figsize=(20,5))
sns.lineplot(x=data["Date"], data=data, y=data["Install events"])
sns.set()
st.pyplot(fig5)

st.subheader("Update events in November 20222")
fig6, ax6 = plt.subplots(figsize=(20,5))
sns.lineplot(x=data["Date"], data=data, y=data["Update events"])
sns.set()
st.pyplot(fig6)

st.subheader("Uninstall events in November 20222")
fig7, ax7 = plt.subplots(figsize=(20,5))
sns.lineplot(x=data["Date"], data=data, y=data["Uninstall events"])
sns.set()
st.pyplot(fig7)

