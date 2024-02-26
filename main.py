import streamlit as st
from open_ai_gpt import ChatBot
from YOLO_face_detection import FaceDetector


st.title('Neuro_tool_v_1_1')
st.subheader(
    'Это проект "Нейросетевого мультитула". Суть в том, что здесь \
        собраны воедино несколько нейросетевых инструментов. \
            Для выбора модели используй выпадающий список.')

models = ['GPT 3.5_turbo', 'YOLO_face_detecton']
selected_model = st.selectbox('Выберите модель: ', models)

if selected_model == 'GPT 3.5_turbo':
    chat_bot = ChatBot()
    chat_bot.run()

elif selected_model == 'YOLO_face_detecton':
    face_detector = FaceDetector()
    face_detector.run()