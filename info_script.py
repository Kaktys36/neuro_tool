import streamlit as st

def info_func(info, show_info):    
    info_toggle = st.checkbox('Показать/Скрыть информацию о проекте')

    if info_toggle:
        show_info = True
    else:
        show_info = False

    if show_info:
        infos = ['Манифест', 'Поддержать проект', 'Контакты', 'Последние обновления', 'Выражаю благодарность']
        selected_info = st.selectbox('Информация о проекте.', infos, index=0)

    if 'selected_info' in locals():  # Проверяем, определена ли переменная selected_info
        if selected_info == 'Манифест': # Возможен переход на словарь для большей читаемости, но пока просто подпишу комментариями что есть что
            st.text(info[0])
        elif selected_info == 'Поддержать проект':
            st.text(info[1])
        elif selected_info == 'Контакты':
            st.text(info[2])
        elif selected_info == 'Последние обновления':
            st.text(info[3])
        elif selected_info == 'Выражаю благодарность':
            st.text(info[4])
    else:
        pass

