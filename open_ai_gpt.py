import streamlit as st
import random
from openai import OpenAI
class ChatBot:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["API_KEY"]) # Подключение к профилю через API

    def run(self): # Функция запуска модели для вызова из main
        st.title('ChatGPT_3.5_turbo')
        st.subheader('''
                    Я могу писать конспекты, решать математические задачи, написать с нуля эссе на любую тему и многое другое!\n
                    Воспользуйтесь сайдбаром (стрелочка слева вверху) для более детальной настройки.
                     ''')
        
        # Инициализация версии gpt 
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-3.5-turbo"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        scenario_examples = [
            'Запомни: отыгрывай роль пирата. Ты сражаешься с кораблём-призраком. Ты будешь говорить что ты можешь сделать, а я буду тебе помогать, чтобы ты вышел победителем', 
            'Запомни: представь, что ты астронавт, который потерпел крушение на Марсе. Ты будешь предлагать варианты дальнейших действий, а я направлять тебя',
            'Запомни: до этого мы говорили о детских мечтах. Представь, что ты сказал, что мечтал в детстве стать киборгом.',
            'Запомни: проконсультируй меня как профессиональный садовод. Я хочу вырастить несколько расстений мне нужны подробные инструкции.',
            'Запомни: выполни роль киберспортивного тренера. Я хочу знать всё о том, как подноть свой MMR.',
            'Запомни: мы говорили про насекомых, говори только про них. Своди все диалоги к ним.'
            'Запомни: говори только о котиках, своди все разговоры к ним.'
                             ]
        if st.sidebar.checkbox("Добавить сценарий"):
            rand_scenario = random.choice(scenario_examples)
            st.sidebar.markdown('''
                            Данная функция позволяет 
                            персонализировать чат-бот 
                            под вас.
                            Вы можете попросить его 
                            отыгрывать определённую 
                            роль, например, математика.
                            Тогда, чат бот 
                            будет настроен 
                            на решение задачек
                            и объяснение 
                            математический теорий,
                            терминов и т.п.\n
                            Или же скажите, что будете 
                            играть в игру.
                            Пускай бот считает
                            себя астронавтом,
                            который застрял на Марсе 
                            или пиратом, судно которого 
                            штурмует корабль-призрак, 
                            а вы будете говорить, 
                            как ему поступить дальше!
                            В поле указаны примеры сценариев.
                            Если что-то пошло не так, или
                            бот забыл роль, то нужно
                            перезагрузить страницу.
                            ''')
            
            if scenario := st.chat_input(rand_scenario):
                print('12312')
            #user_scenario = st.chat_input(str(rand_scenario))
            #scenario = user_scenario
            #st.session_state.messages.append({'role': 'system', 'content': scenario})
        else:
            pass

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input('Поле для ввода запроса.'):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for response in self.client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                ):
                    full_response += (response.choices[0].delta.content or "")
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})