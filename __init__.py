
import streamlit as st

from bedrock import call_bedrock_service


class myEvent:
    question = "XXXXXXXX"


st.title("NIST AI Agent :sunglasses:")
st.markdown(''':grey[Ask me any thing about NIST Cybersecurity Framework - ]''')
st.markdown(''':grey[What are the subcategories of the CSF 2.0 Core?]''')
st.markdown(''':grey[What are supply chain risks? ]''')
st.markdown(''':grey[what is GV.OC-04?]''')

show_gif = False
with st.form(key="question_form", clear_on_submit=True):
    prompt = st.text_input("", "")
    button = st.form_submit_button("Submit")
    agent_message = "NIST AI Agent searching millions of pages to find the answer for you. Please wait for a moment...:sunflower:  "
    agent_response = ""
    
    question_text = st.empty()
    agent_response_text = st.empty()
    agent_text = st.empty()
    if button:
        show_gif = True
        agent_text.subheader(''':blue[{temp}]'''.format(temp=agent_message))
        question_text.markdown(''':orange[{temp}]'''.format(temp=prompt))
        agent_response = call_bedrock_service(prompt)
        agent_response_text.write(agent_response)
        agent_message = ""
        agent_text.caption(''':blue[{temp}]'''.format(temp=agent_message))
        show_gif = False
         


# if __name__ == '__main__':
#     main()
