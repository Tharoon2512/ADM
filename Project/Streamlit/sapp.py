import streamlit as st
import pandas as pd
import numpy as np



 

st.title('Apple iPhone Review System')
st.markdown('This application is meant to **_assist_ _Customers_ _in_ Choosing an iPhone model based on Reviews**, The customers would detrmne the purchase of their iphone models based on previous customer purchases')

df = pd.read_csv('C:\\Users\\lokes\\srcs\\streamlit_app\\result.csv')
df1 = pd.read_csv('C:\\Users\\lokes\\srcs\\streamlit_app\\ReviewCount.csv')

def get_splited_df_dict(df: 'pd.DataFrame', split_column: 'str'):
    """
    splits a pandas.DataFrame on split_column and returns it as a dict
    """

    df_dict = {value: df[df[split_column] == value] for value in df[split_column].unique()}

    return df_dict

splitted = get_splited_df_dict(df, "PRODUCT")
splitted_1 = get_splited_df_dict(df1, "Products")
if st.checkbox('Show me Training Data'):
	st.dataframe(df)
 

_input = str(st.text_input("Enter Model to Search"))
n=0
for index, row in df.iterrows():
       if (row["PRODUCT"] == _input)and n==0:
            des_df = splitted['%s'%(_input)]
            des_df["DESCRIPTION"]
            des_df.reset_index(drop=True, inplace=True)
            n+=1

n=0
for index, row in df1.iterrows():
       if (row["Products"] == _input)and n==0:
            pos_df = splitted_1['%s'%(_input)]
            pos_df["Positive"]
            pos_df["Negative"]
            pos_df.reset_index(drop=True, inplace=True)
            n+=1
