import whisper
import streamlit as st

class Transcriber:
    def __init__(self, whisper_model: str, translation: bool):
        self.translation = False
        self.whisper_model = 'base'
        
    def run():
        st.title("Whisper")
        #if st.sidebar.form("input_form"):
         #   input_files = st.file_uploader("Files", type=["mp4", "m4a", "mp3", "wav"], accept_multiple_files=True)

           # whisper_model = st.selectbox("Whisper model", options=[
           # "tiny", "base", "small", "medium", "large"], index=4)
