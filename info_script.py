import streamlit as st

def info_func(info, session_status):    
    if session_status.show_start_page:
        info_btn = st.button('Показать/Скрыть информацию о проекте')

        if info_btn:
            if 'show_info' not in session_status or not session_status.show_info:
                st.session_state.show_info = True
            else:
                st.session_state.show_info = False

        if st.session_state.show_info:
            infos = ['Манифест', 'Поддержать проект', 'Контакты', 'Последние обновления', 'Выражаю благодарность']
            selected_info = st.selectbox('Информация о проекте.', infos)

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