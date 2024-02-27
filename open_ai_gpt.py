import streamlit as st

from openai import OpenAI
class ChatBot:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["API_KEY"])

    def run(self):
        st.title('ChatGPT 3.5 turbo')
        st.subheader('Я могу писать конспекты, решать математические задачи, написать с нуля эссе на любую тему и многое другое!')

        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-3.5-turbo"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        st.markdown("""
        <style>
        div[data-baseweb="input"] {
            margin-top: -100px;  # Меняйте значение, чтобы придать нужное смещение
        }
        </style>
        """, unsafe_allow_html=True)
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Спрашивай то что хочешь узнать!"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for response in self.client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                ):
                    full_response += (response.choices[0].delta.content or "")
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})