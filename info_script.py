import streamlit as st


def info_func(info, show_info): # Функция для отображения информации о проекте по разделам
    infos = ['Манифест', 'Поддержать проект', 'Контакты', 'Последние обновления', 'Выражаю благодарность', 'Политика использования'] # Определение переменной с названиями категорий информации
    info_toggle = st.checkbox('Показать/Скрыть информацию о проекте') # Добавление в переменную info_toggle чекбокса

    if info_toggle:  # Если чекбокс прожат, то 
        show_info = True  # Значение show_info принимает True и позже идёт обработка отображения информации
    else:
        show_info = False # Иначе False и информация отображаться не будет

    if show_info: # И так, если чекбокс нажат, то show_info = True и
        selected_info = st.selectbox('', infos, index=0) # В переменной selected_info находится выпадающий список (st.selectbox) без подписи, который принимает на вход список infos, названия категорий отображаются при нажатии на selectbox. index=0 отображает первый переданный элемент (Манифест)

    if 'selected_info' in locals():  # Проверяем, определена ли переменная selected_info. Переменная selected_info определена внутри функции, что позволяет установить проверку на её локальность
        
        if selected_info == 'Манифест': # Собственно дальше проверки того, что выбрано в selectbox. Если Манифест, то
            st.markdown(info['manifest']) # С помощью st.markdown отображается текст из переменной manifest из списка info (под индексом 0)
        elif selected_info == 'Поддержать проект':
            st.markdown(info['requisites']) 
        elif selected_info == 'Контакты':
            st.markdown(info['contacts']) 
        elif selected_info == 'Последние обновления':
            st.markdown(info['update_info']) 
        elif selected_info == 'Выражаю благодарность':
            st.markdown(info['gratitude']) 
        elif selected_info == 'Политика использования':
            st.markdown(info['term_of_use'])
    else:
        pass
