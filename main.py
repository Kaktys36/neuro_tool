import streamlit as st
from open_ai_gpt import ChatBot
from YOLO_face_detection import FaceDetector
from info_script import info_func
from info_data import info

# Инициализация сессионного состояния
session_status = st.session_state
if "show_start_page" not in session_status:
    session_status.show_start_page = True
    session_status.show_info = False

if session_status.show_start_page:
    st.title('Neuro_tool_v.1.1')
    st.subheader(
       'Это проект "Нейросетевого мультитула". Суть в том, что здесь собраны воедино несколько нейросетевых инструментов. Всё доступно каждому и абсолютно бесплатно (подробнее в информация_о_проекте>манифест).')

    session_status.show_start_page = False

models = ['Выбрать модель', 'GPT 3.5_turbo', 'YOLO_face_detecton']

if not session_status.show_start_page:
    selected_model = st.selectbox('Выберите модель: ', models)

    if selected_model == 'GPT 3.5_turbo':
        chat_bot = ChatBot()
        chat_bot.run()

    elif selected_model == 'YOLO_face_detecton':
        face_detector = FaceDetector()
        face_detector.run()

    elif selected_model == 'Выбрать модель':
        session_status.show_start_page = True

info_func(info, session_status)