import os
import openai

def generate_answer(question):
    openai.api_key =  st.secrets["OPENAI_KEY"]
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt='Please generate answer for the question: ' + question,
    temperature=0.7,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\""]
    )

    return response
