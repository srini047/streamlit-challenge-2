import streamlit as st
import pandas as pd

data = pd.read_csv('./jina-faq.csv')

st.title('Dashboard')
edited_df = st.experimental_data_editor(
    data,
    num_rows="dynamic",
)
