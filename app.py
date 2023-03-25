# Importing libraries
import streamlit as st
import pandas as pd
import time

# Import OpenAI response generator
from answer import generate_answer


@st.cache
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')


# App title
st.title('🔰FAQ Answer Generator🔰')

# Upload file
uploaded_file = st.file_uploader('Please upload your FAQ\'s file with only one column heading same as `question`', type=[
                                 '.csv'], disabled=True, accept_multiple_files=False, label_visibility="visible")

# Read data
df = pd.read_csv('./jina-faq.csv')

# Show the editor after clicking on the button
if (st.button('Click to generate answers👈')):
    # Run the OpenAI prompt
    df['ai-generated-answer'] = df.apply(
        lambda x: generate_answer(x['question']), axis=1)

    # Spinner to load the answers after running the prompt on FAQs
    with st.spinner('Loading your answers...'):
        time.sleep(5)

    st.balloons()
    # st.success('Successfully generated answers!!!', icon="✅")

# Heart of the application i.e. the data editor
edited_df = st.experimental_data_editor(
    df,
    use_container_width=True,
    num_rows='fixed'
)

edited_df = convert_df_to_csv(edited_df)

# Downlaod answers
st.download_button(
    label="Download generated answers as CSV",
    data=edited_df,
    file_name='generated-answers.csv',
    mime='text/csv',
)
