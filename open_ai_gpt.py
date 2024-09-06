import streamlit as st  # Импортируем библиотеку Streamlit
from openai import OpenAI  # Импортируем библиотеку OpenAI

class ChatBot:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["API_KEY"])  # Подключение к OpenAI с использованием ключа API из Streamlit Secrets (это стандарт, и это секурно)

    def run(self):  # Функция для запуска чатбота
        st.title("ChatGPT 3.5 Turbo")  # Заголовок в приложении Streamlit
        st.subheader("""  
                    ChatGPT прекрасно работает с текстом (и кодом тоже): конспекты, задачи, генерация и редактирование текста - мы до конца не знаем, на что он способен.\n
                    Пробуйте!\n
                    Более подробные настройки открываются по стрелке в панели слева сверху.
                     """)  # Расскажем пользователю, что делает этот чатбот и как им пользоваться

        # Инициализация версии GPT
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-3.5-turbo-0125"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Проверка, хочет ли пользователь фиксировать ответы на определённом языке
        if st.sidebar.toggle('Фиксировать ответы на определённом языке'):
            if st.sidebar.button('English'): 
                st.session_state.messages.append({'role': 'system', 'content': 'Теперь только по-английски'})
            if st.sidebar.button('Русский'):
                st.session_state.messages.append({'role': 'system', 'content': 'Теперь только по-русски'})

        # Проверка, хочет ли пользователь добавить сценарий
        if st.sidebar.toggle('Добавить сценарий'):
            if st.button('Информация о сценарии'):
                st.markdown('''
                       ChatGPT - это прекрасный актёр. Он может отыгрывать любую роль какую попросите.
                       Для того, чтобы попробовать, загрузите здесь фиксированный текстовый промпт в формате .txt и нажмите кнопку "Отправить сценарий"\n
                       Промпт должен быть написан от имени ChatGPT:\n
                       Пример: Я виртуальный помощник, играющий роль очень опытного программиста-сеньора.\n
                       Пример: Мы играем в ролевую игру. Я капитан корабля, который атаковал Летучий Голландец, полный злобных пиратов-призраков. Помоги мне спасти команду и одержать верх.
                        ''')
            
            # Принимаем файл со сценарием от пользователя
            uploaded_file = st.file_uploader("Выберите файл", type=["txt"])
            if uploaded_file is not None:
                text = uploaded_file.read()
                decoded_text = text.decode("utf-8")
                scenario_button = st.button('Отправить сценарий')
                if scenario_button:
                    st.session_state.messages.append({'role': 'system', 'content': decoded_text})
        
        # Собственно реализуем чат
        for message in st.session_state.messages:
            # Отображает сообщения из списка messages в чате
            with st.chat_message(message['role']):
                st.markdown(message['content'])

        # Поддержка ввода текстового запроса от пользователя
        if prompt := st.chat_input('Поле для ввода запроса.'):
            # Добавление пользовательского запроса в список сообщений
            st.session_state.messages.append({'role': 'user', 'content': prompt})
            with st.chat_message('user'):
                # Отображает сообщение пользователя в чате
                st.markdown(prompt)

            with st.chat_message('assistant'):
                message_placeholder = st.empty()
                full_response = ''
                # Перебор ответов от чатбота для формирования полного ответа
                for response in self.client.chat.completions.create(
                        model=st.session_state['openai_model'],
                        messages=[{'role': m['role'], 'content': m['content']} for m in st.session_state.messages],
                        stream=True,
                ):
                    # Добавление новой части ответа к общему ответу
                    full_response += (response.choices[0].delta.content or '')
                    # Посимвольное отображение промежуточного ответа с красивым бегущим указателем
                    message_placeholder.markdown(full_response + '▌')
                # Отображение окончательного ответа
                message_placeholder.markdown(full_response)
            # Добавление ответа от чатбота в список сообщений - так бот будет помнить, что пользователь спрашивал в этой сессии
            st.session_state.messages.append(
                {'role': 'assistant', 'content': full_response}
            )
