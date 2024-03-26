import streamlit as st
import random
from openai import OpenAI  # Загрузка библиотеки для работы c GPT


class ChatBot:
    def __init__(self):
        self.client = OpenAI(
            api_key=st.secrets["API_KEY"]
        )  # Подключение к профилю через API

    def run(self):  # Функция запуска модели для вызова из main
        st.title("ChatGPT_3.5_turbo")
        st.subheader(
            """
                    Я могу писать конспекты, решать математические задачи, написать с нуля эссе на любую тему и многое другое!\n
                    Воспользуйтесь сайдбаром (стрелочка слева вверху) для более детальной настройки.
                     """
        )

        # Инициализация версии gpt
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-3.5-turbo"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        if st.sidebar.toggle('Добавить сценарий'):
            if st.button('Информация сценарии'):
                st.markdown('''
                       Функция работает в тестовом формате и доступна только через загрузку текстового файла.\n
                       Для того, чтобы воспользоваться ей необходимо отправить текстовый файл в формате txt
                       (обычный блокнот) и после этого нажать кнопку "Отправить сценарий".\n При составлении сценария пишите от имени GPT:\n
                       Пример: Я виртуальный помощник, отыгрывающий роль программиста-сеньора.
                       Прмиер: Я капитан корабля, на который напал корабль-призрак. Помоги мне выйти с победой из сложившейся ситуации. мы играем в ролевую игру.
                        '''
                )

            uploaded_file = st.file_uploader("Выберите файл", type=["txt"])
            if uploaded_file is not None:
                text = uploaded_file.read()
                decoded_text = text.decode("utf-8")
                scenario_button = st.button('Отправить сценарий')
                if scenario_button:
                    st.session_state.messages.append({'role': 'system', 'content': decoded_text})

        for message in st.session_state.messages:
            with st.chat_message(message['role']):
                st.markdown(message['content'])

        if prompt := st.chat_input('Поле для ввода запроса.'):
            st.session_state.messages.append({'role': 'user', 'content': prompt})
            with st.chat_message('user'):
                st.markdown(prompt)

            with st.chat_message('assistant'):
                message_placeholder = st.empty()
                full_response = ''
                for response in self.client.chat.completions.create(
                        model=st.session_state['openai_model'],
                        messages=[
                            {'role': m['role'], 'content': m['content']}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                ):
                    full_response += (response.choices[0].delta.content or '')
                    message_placeholder.markdown(full_response + '▌')
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({'role': 'assistant', 'content': full_response})
