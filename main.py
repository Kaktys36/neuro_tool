import streamlit as st
from open_ai_gpt import ChatBot
from YOLO_face_detection import FaceDetector
from info import info

show_start_page = True
if show_start_page:
    st.title('Neuro_tool_v.1.1')
    st.subheader(
       'Это проект "Нейросетевого мультитула". Суть в том, что здесь \
        собраны воедино несколько нейросетевых инструментов. Всё доступно каждому и абсолютно бесплатно (подробнее в манифесте).')

models = ['GPT 3.5_turbo', 'YOLO_face_detecton']
selected_model = st.selectbox('Выберите модель: ', models)

if selected_model == 'GPT 3.5_turbo':
    chat_bot = ChatBot()
    chat_bot.run()

    re_btn =  st.button("Вернуться к начальной странице")
    if re_btn:
        show_start_page = False
        st.rerun()

elif selected_model == 'YOLO_face_detecton':
    face_detector = FaceDetector()
    face_detector.run()

    re_btn =  st.button("Вернуться к начальной странице")
    if re_btn:
        show_start_page = False
        st.rerun()

infos = ['Манифест', 'Поддержать проект']
selected_info = st.selectbox('Информация о проекте.', info)

if selected_info == 'Манифест':
    st.write(info[0])
elif selected_info == 'Поддержать проект':
    st.write(info[1])
elif selected_info == 'Контакты':
    st.write(info[2])
elif selected_info == 'Последние обновления':
    st.write(info[3])