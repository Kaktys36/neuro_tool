import streamlit as st
from open_ai_gpt import ChatBot
from YOLO_face_detection import FaceDetector
from info import info

# Инициализация сессионного состояния
if "show_start_page" not in st.session_state:
    st.session_state.show_start_page = True
    st.session_state.show_info = False

if st.session_state.show_start_page:
    st.title('Neuro_tool_v.1.1')
    st.subheader(
       'Это проект "Нейросетевого мультитула". Суть в том, что здесь \
        собраны воедино несколько нейросетевых инструментов. Всё доступно каждому и абсолютно бесплатно (подробнее в манифесте).')

    models = ['GPT 3.5_turbo', 'YOLO_face_detecton']
    selected_model = st.selectbox('Выберите модель: ', models)

    if selected_model == 'GPT 3.5_turbo':
        chat_bot = ChatBot()
        chat_bot.run()

    elif selected_model == 'YOLO_face_detecton':
        face_detector = FaceDetector()
        face_detector.run()

    st.session_state.show_start_page = False

elif st.session_state.show_info:
    infos = ['Манифест', 'Поддержать проект', 'Контакты', 'Последние обновления', 'Выражаю благодарность']
    selected_info = st.selectbox('Информация о проекте.', infos)

    if selected_info == 'Манифест':
        st.text(info[0])
    elif selected_info == 'Поддержать проект':
        st.text(info[1])
    elif selected_info == 'Контакты':
        st.text(info[2])
    elif selected_info == 'Последние обновления':
        st.text(info[3])
    elif selected_info == 'Выражаю благодарность':
        st.text(info[4])

    st.session_state.show_info = False

else:
    st.button("Показать информацию о проекте")
    if st.button_clicked("Показать информацию о проекте"):
        st.session_state.show_info = True