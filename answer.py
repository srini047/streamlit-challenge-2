import streamlit as st
import openai

def generate_answer(question, company):
    if(company == ''):
        company = 'JinaAI'
    openai.api_key =  st.secrets["OPENAI_KEY"]
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt='Please generate answers for these FAQ\'s in terms of' + company + ': ' + question,
    temperature=0.7,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\""]
    )

    substring = '\n\n'
    ans = response.choices[0].text
    if(ans.startswith(substring)):
        ans = ans[len(substring):]

    return ans
