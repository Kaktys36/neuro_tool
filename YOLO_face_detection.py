class FaceDetector:
    def __init__(self):
        # download model
        model_path = hf_hub_download(repo_id='arnabdhar/YOLOv8-Face-Detection', filename='model.pt')
        self.model = YOLO(model_path)

    def run(self):
        uploaded_file = st.file_uploader('Выберите изображение (jpg, jpeg, png)', type=['jpg', 'jpeg', 'png'])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            output = self.model(image)
            results = Detections.from_ultralytics(output[0])
            st.write(f'Модель обнаружила на фотографии {len(results)} лиц людей')
