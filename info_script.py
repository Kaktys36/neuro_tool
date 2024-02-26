import streamlit as st

def click_button():
    st.session_state.button = not st.session_state.button

def info_func(info, show_info, show_start_page):    
    if 'button' not in st.session_state:
        st.session_state.button = False

    if show_start_page:
        info_btn = st.button('Показать/Скрыть информацию о проекте', on_click=click_button)
        print(info_btn)

        if info_btn:
            show_info = True
        elif not info_btn:
            show_info = False

        if show_info:
            infos = ['Манифест', 'Поддержать проект', 'Контакты', 'Последние обновления', 'Выражаю благодарность']
            selected_info = st.selectbox('Информация о проекте.', infos, index=0)

        if 'selected_info' in locals():  # Проверяем, определена ли переменная selected_info
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
        else:
            pass