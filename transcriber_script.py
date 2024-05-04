import whisper
import streamlit as st
#import torch

model: whisper.Whisper = None
modelName: str = "base.en"
class Transcriber:
    def __init__(self):
        self.test = 'asdas',
        self.whisper_model = "base"
       # @st.cache_resource(show_spinner=False)
        
    def load_whisper_model(self, modelName: str) -> whisper.Whisper:
        try:
            global model
            model = whisper.load_model(modelName)
            print("Model Loaded")
            print("-------------------------")
            return model
        except Exception as e:
            st.error(f"Failed to load Whisper model: {e}", icon="❌")
        
    def run(self):
        st.title("Whisper")
        st.subheader(
            """
            Я могу писать транскрибировать аудио и видеофайлы (получать текст).
            """
        )
        self.input_file = st.sidebar.file_uploader("Files", type=["mp4", "m4a", "mp3", "wav"])

        self.whisper_model = st.sidebar.selectbox("Whisper model", options=[
            "tiny", "base", "small", "medium", "large", "large-v2", "large-v3"], index=4)
        self.model = self.load_whisper_model(self.whisper_model)
    
        
   