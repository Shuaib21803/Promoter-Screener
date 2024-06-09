import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

df = pd.read_csv('https://raw.githubusercontent.com/Shuaib21803/Promoter-Screener/main/stocks.csv')
meta = requests.get('https://api.github.com/repos/Shuaib21803/Promoter-Screener/commits?path=stocks.csv').json()[0]['commit']['committer']['date']
meta = ' '.join(meta.split('T'))[0:-1]
df['Pledged'] = df['Pledged'].str.lstrip()
df = df[df["Pledged"].isin(['-','0.00','0'])]
df = df[df['SAST Regulations']=='Yes']
df = df[df['Shareholding'].astype(float)>33.0]
df = df[df['Shareholding'].astype(float)<=75.0]

st_df = df[['symbol', 'secAcq', 'Promoter Buying', 'Current Price','Shareholding', 'Pledged', 'SAST Regulations', 'Financial Results']]
st_df = st_df.reset_index(drop=True)

st.subheader('Raw Data')
#st.markdown(st_df.to_markdown(index=False))
#st.table(st_df)
st.dataframe(st_df)
st.write("Last updated:",meta)