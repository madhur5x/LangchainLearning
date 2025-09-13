'''
making a simple question answer chabot
'''

import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage ## any outmessages which comes from apt will be mentioned in AIMessages
import os 


## page Config
st.set_page_config(page_title="Simple Langchain usage", page_icon="🦜")

#title
st.title("🦜 Simple Chatboot")
st.markdown("Learning Langchain basics with groq api")

with st.sidebar:
    st.header("Setting")

    ##API KEY
    api_key= st.text_input("Groq API Key",type="password",help="get FREE API key at console.groq.com")

    ## Model Selection
    model_name=st.selection(
        "model",["gemma2-9b-it","openai/gpt-oss-120b"],
        index=0
    )

    ## Clear button
    if st.button("Clear Chat"):
        st.session_state.message = []
        st.rerun()

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

## Inintialize LLM
@st.cache_resource
def get_chain(api_key,model_name):
    if not api_key:
        return None

    ## Initialize the groq Model
    ChatGroq(groq_api_key=api_key,
             model_name=model_name,
             tempreature=0.7,
             streaming=True)


