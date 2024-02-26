import streamlit as st
from openai import OpenAI
from open_ai_gpt import ChatBot
from YOLO_face_detection import FaceDetector
from huggingface_hub import hf_hub_download
from ultralytics import YOLO
from supervision import Detections
from PIL import Image

st.title('Neuro_tool_v_1_1')
st.subheader('Это проект "Нейросетевого мультитула. Суть в том, что здесь собраны воедино несколько нейросетевых инструментов. Для выбора модели используй выпадающий список."')

models = ['GPT 3.5_turbo', 'YOLO_face_detecton']
selected_model = st.selectbox('Выберите модель: ', models)

if selected_model == 'GPT 3.5_turbo':
    chat_bot = ChatBot()
    chat_bot.run()

elif selected_model == 'YOLO_face_detecton':
    face_detector = FaceDetector()
    face_detector.run()