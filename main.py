import streamlit as st
from open_ai_gpt import ChatBot # Импорт класса ChatBot из файла open_ai_gt. Содержит метод run для запуска 
from YOLO_face_detection import FaceDetector # Импорт класса FaceDetector из файла YOLO_face_detection. Содержит метод run для запуска 
from info_script import info_func # Импорт функии info_func для отображения информации о проекте. На вход необходима информация
from info_data import info # Импорт переменной info из info_data (список)

show_start_page = True # Булевая переменная для определения необходимости отображения информации только стартовой страницы (информация о проекте и заголовок)
show_info = False # Булевая переменная для определения необходимости отображения подробной информации о проекте. Она используется в info_func и нужна чтобы изначально более подробная информация не отображалась, но при необходимости  её можно было отобразить, кликнув на checkbox

models = ['Стартовая страница', 'GPT_3.5_turbo', 'YOLO8_face_detector'] # Список, который передаётся в selectbox (выпадающий список) для обработки того, какую модель запустить
selected_model = st.selectbox('Выберите модель: ', models) # Запись в переменную selected_model выбранной модели из st.selectbox


if selected_model == 'GPT_3.5_turbo': # Если выбран GPT_3.5_turbo
    chat_bot = ChatBot() # Запись класса с ботом в переменную
    chat_bot.run() # Запуск бота
    show_start_page = False # Переопределение переменной show_start_page для остановки показа информации со стартовой страницы

elif selected_model == 'YOLO8_face_detector': # Тоже самое, только для класса FaceDetector c YOLO8
    face_detector = FaceDetector()
    face_detector.run()
    show_start_page = False

else:
    show_start_page = True # Иначе стартовая показ информации со стартовой страницы сохраняется

if show_start_page: # Если переменная True, то
    st.title('Neuro_tool_v.1.1') # Будет этот заголовок 
    st.subheader('''
                    Это проект "Нейросетевого мультитула". 
                    Суть в том, что здесь собраны воедино несколько нейросетевых инструментов.
                    Всё доступно каждому и абсолютно бесплатно (подробнее в "Информация о проекте" > "Манифест").
                 ''') # И этот подзаголовок
    info_func(info, show_info, show_start_page) # И будет возможность посмотреть более подробную информацию. Функция нужна для отображения подробной информации. Получает переменную info (список с переменными, в которых информация разбита на логические части), булевую переменную show_info для определения необходимости отображения/скрытия подробностей и show_start
    
else: # Иначе ничего и никаких заголовкой. Новые заголовки определяются в классах ChatBot и FaceDetector
    pass
