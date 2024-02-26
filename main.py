import streamlit as st
from open_ai_gpt import ChatBot
from YOLO_face_detection import FaceDetector
from info_script import info_func
from info_data import info

show_start_page = True
show_info = False

models = ['Выбрать модель', 'GPT 3.5_turbo', 'YOLO8_face_detector']
selected_model = st.selectbox('Выберите модель: ', models)


if selected_model == 'GPT 3.5_turbo':
    chat_bot = ChatBot()
    chat_bot.run()
    show_start_page = False

elif selected_model == 'YOLO8_face_detecton':
    face_detector = FaceDetector()
    face_detector.run()
    show_start_page = False

else:
    show_start_page = True

if show_start_page:
    st.title('Neuro_tool_v.1.1')
    st.subheader(
       'Это проект "Нейросетевого мультитула". Суть в том, что здесь собраны воедино несколько нейросетевых инструментов. Всё доступно каждому и абсолютно бесплатно (подробнее в информация_о_проекте>манифест).')
else:
    st.title('')
    st.subheader('')

info_func(info, show_info, show_start_page)