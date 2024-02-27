# Файл для хранения данных с подробной информацией. Все переменные отображаются с помощью st.text в info_script(в функции info_func, которая вызывается в main)

# Переменная с обращением к пользователю, содержит общую информацию о политике проекта, идеологии и т.п.
manifest = ''' 
            Привет, пользователь. \n 
            Как ты мог заметить, весь функционал доступен совершенно бесплатно.
            Это всё потому, что по моему мнению, новые нейросетевые инструменты 
            должны быть доступны абсолютно любому и за них не надо платить деньги 
            или изучать программирование, чтобы сделать что-то подобное самому.
            Этот проект развивается на чистом энтузиазме 
            и материальной поддержке неравнодушных.\n 
            Деньги нужны для оплаты доступа к некоторым платным инструментам, 
            как, например, GPT, а также для поддержания мотивации разработчика 
            (в данный момент я ищу работу и хочу кушать XD).\n 
            Если тебе был полезен тот или иной инстумент представленный здесь, 
            то пожалуйста, перешли его другу. \n 
            По возможности ты можешь поддержать разработчика. 
            Все контакты и реквизиты представлены в кнопке "Контакты" и "Поддержать проект".\n
            Разработчик не имеет доступа к вашим запросам, фотографиям и другой информации, 
            которую вы отправляете в нейросети и модели.
            В этом Вы модете убедиться, обратившись к странице проекта на github.
            Тем не меннее, разработчик не несёт ответственности
            за сохранность Ваших данных и их анонимность.
            Используя neurotool, Вы соглашаетесь с политикой использования и
            конфиденциальности всех представленных нейросетей и моделей,
            а также сервиса Streamlit, на котором развёрнуто приложение.\n
            \tStreamlit: https://streamlit.io/terms-of-use
            \tGPT: https://openai.com/policies/usage-policies
            \tYOLO не подразумевает политики использования, так как это просто математическая модель.
            Все вычисления происходят на Streamlit
            '''

# Переменная с информацией о том, как поддержать проект и куда перечислить средства на развитие
requisites = '''
              В данных момент доступны следующие способы:
              \tНомер карты (Сбер, СБП): 2202201869695284
              При переводе просьба указывать коментарий "neurotool".
              \tВ данный момент планируется подключение GPT4 со всеми фишками.
              Стоимость месячного подключения стоит 20$. В данный момент идёт сбор средств 800/2800.
              Функция может быть отключена, если средств с проекта не будет хватать для оплаты подписки на сервис.
              \tТакже я ищу человека с личной айпи камерой для доработки YOLO8.
              Есть идея подключения камер к проекту: пользователь
              подключает поток видео к проекту и настраивает отправку сообшений при
              определённых изменениях. Например, есть видео-няня. Если в её поле зрения
              больше 1 человека, то приходит смс и сообщение на почту.
              Вот эту идею нужно как-то настроить и отладить.
             '''

# Переменная с информацией о контактах и способах связи связаться с разработчиком
contacts = '''
            Сюда можно обратиться за тех.поддержкой,
            просто поболтать или предложить добавить новую фичу:
            \tTelegram: @KiloLex
            \temail: nikolaeff.alexandr2016@yandex.ru
            \tDiscord: sputnik2286
            \tGithub: https://github.com/Kaktys36
            \tGithub проекта: https://github.com/Kaktys36/neuro_tool
            '''

# Переменная с информацией о последних обновлениях проекта
update_info = '''
               От самых новых.\n
               \t27.02.2024 "neurotool_v.1.1.1"
               Незначительно обновлён интерфейс, исправлена проблема перекрытыя поля отправки кнопкой стримлит
               добавлена функция написания сценария или 
               роли для чат-бота GPT_3.5_turbo от имени system, одновлена информация о проекте, 
               добавлено описание кода на github проекта, незначительное улучшение логики кода.
               \t26.02.2024 "neurotool_v.1.1".
               Проект обрёл имя, манифест, добавлена контактная иформация и реквизиты.
               Добавлена функция переключения моделей.
               Добавлена модель YOLO8 с функцией детекции и подсчёта количества лиц на фотографии.\n
               \t31 Dec 2023 "openai_chat_clone".
               Зарождение проекта. Перваая рабочая проба пера, представляющая из
               себя рабочий GPT 3.5 turbo без необходимости VPN, авторизации и т.п.
               '''

# Переменная с информацией о поддержавших проект
gratitude = '''
            Здесь появится Ваше имя если вы поддержали проект (ник или подпись можно оставить
            в комментарии к переводу или прислать мне по контактам).
            Огромное спасибо:
            \t ***the_nickey***
            '''

# Переменная, объединяющая остальные переменные с информацией в список, для удобства передачи в info_func
info = [manifest, requisites, contacts, update_info, gratitude] 
