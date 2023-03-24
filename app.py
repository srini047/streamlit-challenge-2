import streamlit as st
import pandas as pd

data = pd.read_csv('./jina-faq.csv')

# Uplaod file
uploaded_file = st.file_uploader('Please upload your FAQ\'s file with only one column of FAQs', type=['.csv'], accept_multiple_files=False, label_visibility="visible")

# Read data
data = pd.read_csv(uploaded_file)

# Show the editor
st.title('FAQ answer generator')
edited_df = st.experimental_data_editor(
    data,
    num_rows="dynamic",
)
