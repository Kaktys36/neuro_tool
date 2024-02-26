import streamlit as st
from open_ai_gpt import ChatBot
from YOLO_face_detection import FaceDetector

show_start_page = True
if show_start_page:
    st.title('Neuro_tool_v.1.1')
    st.subheader(
       'Это проект "Нейросетевого мультитула". Суть в том, что здесь \
        собраны воедино несколько нейросетевых инструментов. \
        Для выбора модели используй выпадающий список.')

models = ['GPT 3.5_turbo', 'YOLO_face_detecton']
selected_model = st.selectbox('Выберите модель: ', models)

if selected_model == 'GPT 3.5_turbo':
    chat_bot = ChatBot()
    chat_bot.run()

    st.button("Вернуться к выбору модели")
    if st.button:
        st.rerun()

elif selected_model == 'YOLO_face_detecton':
    face_detector = FaceDetector()
    face_detector.run()

    st.button("Вернуться к выбору модели")
    if st.button:
        st.rerun()