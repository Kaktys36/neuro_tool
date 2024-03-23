#Импорт необходимых библиотек
import streamlit as st
import requests

from huggingface_hub import hf_hub_download
from ultralytics import YOLO
from supervision import Detections
from PIL import Image
class FaceDetector:
    def __init__(self):
        # download model
        model_path = hf_hub_download(repo_id='arnabdhar/YOLOv8-Face-Detection', filename='model.pt')
        self.model = YOLO(model_path)

    def run(self):
        st.title('YOLO8 настроенный на распознавание лиц')
        st.subheader('После того как вы загрузите фотографию я посчитаю сколько на ней лиц людей. Эту функцию можно использовать для подсчёта количества людей на фотографии.')
        uploaded_file = st.file_uploader('Выберите изображение (jpg, jpeg, png)', type=['jpg', 'jpeg', 'png'])
        url = st.text_input("Вставьте ссылку на изображение")

        # Загрузка картинок
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            output = self.model(image)
            results = Detections.from_ultralytics(output[0])
            st.write(f'Модель обнаружила на фотографии {len(results)} лиц людей.')
        # Загрузка картинок по url
        elif url:
            image = Image.open(requests.get(url, stream=True).raw)
            output = self.model(image)
            results = Detections.from_ultralytics(output[0])
            st.write(f'Модель обнаружила на фотографии {len(results)} лиц людей.')







