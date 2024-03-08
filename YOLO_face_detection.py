import streamlit as st

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
        #uploaded_file = st.file_uploader('Выберите изображение (jpg, jpeg, png)', type=['jpg', 'jpeg', 'png'])


    #if uploaded_file is not None:
        ##output = self.model(image)
        #results = Detections.from_ultralytics(output[0])
        #st.write(f'Модель обнаружила на фотографии {len(results)} лиц людей.')


    col1, col2 = st.columns([2, 3])
    image = None

    with col1:
        uploaded_file = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])
        url = st.text_input("...or enter image URL:")
        if uploaded_file:
            image = load_image_from_file(uploaded_file)
        elif url:
            try:
                image = load_image_from_url(url)
            except Exception as e:
                st.warning(f"Error loading image from URL: {e}")
                return

        else:
            st.warning("Please upload an image or provide an image URL.")
            return

        if st.button("Classify image") and image:
            predicted_class = classify_image(image)
            st.success(f"Image class: {predicted_class}")

            with col2:
                if image:
                    # To ensure that square images do not use the entire width of the column
                    aspect_ratio = image.width / image.height
                    use_column_width = aspect_ratio > 1.4

                    if uploaded_file:
                        st.image(image, caption="Uploaded image", use_column_width=use_column_width)
                    elif url:
                        try:
                            st.image(image, caption="Image from URL", use_column_width=use_column_width)
                        except Exception as e:
                            st.warning(f"Error loading image from URL: {e}")

                            if __init__ == "__init__":
                                run()




