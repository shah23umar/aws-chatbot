
import streamlit as st

from bedrock import call_bedrock_service


class myEvent:
    question = "XXXXXXXX"


st.title("NCCN AI Agent :sunglasses:")
st.markdown(''':grey[Ask me any thing about NCCN Guidelines for Soft Tissues Sarcoma - ]''')
st.markdown(''':grey[What is soft tissue sarcoma?]''')
st.markdown(''':grey[What is liposarcomas? ]''')
st.markdown(''':grey[what is core needle biopsy?]''')

show_gif = False
with st.form(key="question_form", clear_on_submit=True):
    prompt = st.text_input("", "")
    button = st.form_submit_button("Submit")
    agent_message = "NCCN AI Agent searching the pages to find the answer for you. Please wait for a moment...:sunflower:  "
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
