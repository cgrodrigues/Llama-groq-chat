from groq import Groq
import streamlit as st
import os
from dotenv import load_dotenv



# Function to add the Llama3 indication
def llama3_text():
    # Criar um container para o texto
    st.header("Power by Llama 3 model")



def main():
    st.title("Groq Chat")

    temperature=1.0

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    if "groq_model" not in st.session_state:
        st.session_state["groq_model"] = "llama3-70b-8192"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["groq_model"],
                messages=[
                    {
                        "role": m["role"], 
                        "content": m["content"]
                    }
                    for m in st.session_state.messages
                ],
                # stream=True,
                temperature=temperature,
            ) 
                    
            response = stream.choices[0].message.content
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
# Load Env. Variables
load_dotenv()    

# Put the LLama 3 name in the page
llama3_text()

main()