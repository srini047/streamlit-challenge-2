# Importing libraries
import streamlit as st
import pandas as pd
import time

# Import OpenAI response generator
from answer import generate_answer

# App title
st.title('🔰FAQ Answer Generator🔰')

# Uplaod file
uploaded_file = st.file_uploader('Please upload your FAQ\'s file with only one column heading same as `question`', type=['.csv'], accept_multiple_files=False, label_visibility="visible")

# Read data
data = pd.read_csv(uploaded_file)

# Run the OpenAI prompt
if(data):
    data['ai-generated-answer'] = data.apply(lambda x: generate_answer(x['question']), axis=1)

# Show the editor after clicking on the button
if(st.button('Click to generate answers👈')):

    # Spinner to load the answers after running the prompt on FAQs
    with st.spinner('Loading your answers...'):
        time.sleep(5)

    st.balloons()
    st.success('Successfully generated answers!!!', icon="✅")

    # Heart of the application i.e. the data editor
    edited_df = st.experimental_data_editor(
        data,
        num_rows="dynamic",
    )

    # Downlaod answers
    st.download_button(
        label="Download generated answers as CSV",
        data=edited_df,
        file_name='generated-answers.csv',
        mime='text/csv',
    )
