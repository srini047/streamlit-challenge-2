# Importing libraries
import base64
import streamlit as st
import pandas as pd
import time

# Import OpenAI response generator
from answer import generate_answer

@st.cache
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

# Default values
success = False

# App title
st.title('🔰FAQ Answer Generator🔰')

# Upload file
uploaded_file = st.file_uploader('Please upload your FAQ\'s file with only one column heading same as `question`', type=[
                                 '.csv'], disabled=True, accept_multiple_files=False, label_visibility="visible")

# Read data
df = pd.read_csv('./jina-faq.csv')

# Enter company name for the FAQs
company = st.text_input('Enter company name like JinaAI, Naas.ai etc', required=True)

# Heart of the application i.e. the data editor
st.write('Edit the questions (if required) to generate the right response...\n')
edited_df = st.experimental_data_editor(
    df
)

df = edited_df

# Show the editor after clicking on the button
if (st.button('Click to generate answers👈')):
    # Run the OpenAI prompt
    df['ai-generated-answer'] = df.apply(
        lambda x: generate_answer(x['question'], company), axis=1)

    # Spinner to load the answers after running the prompt on FAQs
    with st.spinner('Loading your answers...'):
        time.sleep(5)

    st.balloons()
    success = True

if (success):
    if st.button('Download edited data as CSV'):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="generated-answers.csv">Download CSV</a>'
        st.markdown(href, unsafe_allow_html=True)
