import whisper
import streamlit as st

class Transcriber:
    def __init__(self):
        self.test = 'asdas'#, whisper_model: str, translation: bool):
        #self.translation = False
        #self.whisper_model = 'base'
        
    def run(self):
        st.title("Whisper")
        st.subheader(
            """
                    Я могу писать транскрибировать аудио и видеофайлы (получать текст).
                     """
        )
        input_files = st.sidebar.file_uploader("Files", type=["mp4", "m4a", "mp3", "wav"], accept_multiple_files=True)

        whisper_model = st.sidebar.selectbox("Whisper model", options=[
            "tiny", "base", "small", "medium", "large"], index=4)
