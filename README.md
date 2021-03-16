Проект по созданию прототипа сервиса по  ведению медицнских карточек больных больницы РАН  
В данном проекте предствален api сервис прототипа  

Администратор, пароль Администратор с правами врача и и администратора
user1 пароль user1 с правами врача


Функция авторизации администратора
адрес : /check_admin, method POST.
Принимает параметры:
log - имя пользователя
pass - пароль - в MD5

Возвращает результат типа:
{'answer': 1, 'Error': [], 'info_key': {'id': 1, 'username': 'Администратор', 'kye': '39f6b18ee6fd060f8d5c1c6d1118dd44'}}
'answer' - если 1 то авторизация успешная, если ноль то авторизация не прошла.
В поле 'info_key' информация о ключе пользователя
НЕ успешная авторизация
{'answer': 0, 'Error': [{'тип': 'Не пройдена авторизация', 'exeption': 'Не верный логин или пароль'}]}

функция авторизации врача
адрес : /check_doctor, method POST.
Принимает параметры:
log - имя пользователя
pass - пароль - в MD5

Возвращает результат типа:
{'answer': 1, 'Error': [], 'info_key': {'id': 2, 'username': 'user1', 'kye': '39f6b18ee6fd060f8d5c1c6d1118dd44'}}
'answer' - если 1 то авторизация успешная, если ноль то авторизация не прошла.
В поле 'info_key' информация о ключе пользователя
НЕ успешная авторизация
{'answer': 0, 'Error': [{'тип': 'Не пройдена авторизация', 'exeption': 'Не верный логин или пароль'}]}

Функция запроса списка пользователей
/list_users",methods=['GET']

Передает параметр key. Если key валидный отправляется список полей таблицы users:
id,Username,FirstName,MiddlName,SacondName,Birthday,ProfSpacial,Doctor,Admin,off

Пример ответа: {'answer': 1, 'data': [[1, 'Администратор', 'Администратор', None, None, None, None, 1, 1, 0], [2, 'user1', 'Иванов', None, None, None, None, 1, 0, 0]]}

Если попытка будет не удачная по каким то причинам, то ключ ‘answer’= 0. И описание ошибки
Пример отрицательного ответа:
{'answer': 0, 'error': 'Не найден ключ', 'comment': 'Не удалось подтвердить действие ключа'}

4. Функция добавления пользователя. Ее может делать только администратор
ame,
/insert_users",methods=['PUT']
Передаем:
key - ключ пользователя который отправляет данные,
Username,
password (MD5),
FirstName,
MiddlNSacondName,
Birthday формат : 1979-11-22,
ProfSpacial,
Doctor булево,
Admin булево,
off булево

Если какие то поля пустые передаем Null, но количество полей должно быть полным и в такой же последовательности


5.Функция изменения пользователя
/update_users",methods=['PATCH']
Уславиливаемся что Username  - не меняем
Пароль меняем отдельным запросом

Передаем:
key - ключ пользователя который отправляет данные,
FirstName,
MiddlName,
SacondName,
Birthday формат : 1979-11-22,
ProfSpacial,
Doctor булево,
Admin булево,
off булево,
id

Если какие то поля пустые передаем Null, но количество полей должно быть полным и в такой же последовательности

В случае успеха ответа ключ answer приходит =1, иначе 0 с информацией об ошибках

6. Функция смены пароля пользователя
"/update_password",methods=['PATCH']

Передаем : ['key','pass','id']
pass - уже новый pass в MD5

В случае успеха ответа ключ answer приходит =1, иначе 0 с информацией об ошибках


7. Получения списка анкет пациентов,
"/list_pacients",methods=['GET']

Передает параметр key. 
Если key валидный отправляется список всех строк таблицы pacients:

'answer': 1 в случае успеха + данные, 'answer': 0 в случае не успеха, плюс информация об ошибке.

Пример ответа:

{'answer': 1, 'data': [{'id': 1, 'Doctor_id': 2, 'FirstName': 'Алексей', 'MiddlName': 'Иванович', 'SacondName': 'Пирогов', 'Birthday': '02-23-1965', 'Sex': 0, 'Adres': 'Санкт Петерг, проезд рыжего дядьки 48', 'Phone': '+7958256378', 'Anamnes': 'Неделю болит голова', 'Diagnos': 'ОНМК ?', 'PersDastaSoglasie': 1, 'SoglasieMed': 1, 'created_at': '10-16-2020', 'updated_at': '10-16-2020'}, {'id': 2, 'Doctor_id': 3, 'FirstName': 'Игорь', 'MiddlName': 'Сергеевич', 'SacondName': 'Попов', 'Birthday': '02-23-1975', 'Sex': 0, 'Adres': 'Санкт Петербург, ул  Лени Голикого 456', 'Phone': '+7958256378', 'Anamnes': 'Живот болит 3 дня, Диарея', 'Diagnos': 'Отравление ?', 'PersDastaSoglasie': 1, 'SoglasieMed': 1, 'created_at': '10-16-2020', 'updated_at': '10-16-2020'}, {'id': 3, 'Doctor_id': 4, 'FirstName': 'Илья', 'MiddlName': 'Иванович', 'SacondName': 'Козлов', 'Birthday': '02-28-1980', 'Sex': 0, 'Adres': 'Санкт Петербург, ул  Оптиков д 4', 'Phone': '+7958256378', 'Anamnes': 'Глдаз маргает третий день', 'Diagnos': 'Маргоглазка ?', 'PersDastaSoglasie': 1, 'SoglasieMed': 1, 'created_at': '10-16-2020', 'updated_at': '10-16-2020'}]}

Отрицательный:
 {'answer': 0, 'error': 'Не найден ключ', 'comment': 'Не удалось подтвердить действие ключа'}


8. Функция /insert_pacient",methods=['PUT']
Добавляем новую анкету пациента .
Нужно передать:
'key' ключ авторизации,
'Doctor_id',
'FirstName',
'MiddlName',
'SacondName',
'Birthday' - в формате 1979-11-22 ,
'Sex' М или Ж,
'Adres',
'Phone',
'Anamnes'
,'Diagnos',
'PersDastaSoglasie' - 1
,'SoglasieMed' - 1

Передать нужно ВСЕ поля, пустые - ‘Null’
В ответ приходит
'answer': 1 в случае успеха, 'answer': 0 в случае не успеха, плюс информация об ошибке.

9. Функция обновления анкеты /update_pacient",methods=['PATCH']
Изменяем анкету пациента:
Нужно передать:
'key' ключ авторизации,
'Doctor_id',
'FirstName',
'MiddlName',
'SacondName',
'Birthday' - в формате 1979-11-22 ,
'Sex' М или Ж,
'Adres',
'Phone',
'Anamnes'
,'Diagnos',
'PersDastaSoglasie' - 1
,'SoglasieMed' - 1
id - id анкеты



Передать нужно ВСЕ поля, пустые - ‘Null’
В ответ приходит
'answer': 1 в случае успеха, 'answer': 0 в случае не успеха, плюс информация об ошибке.

10. функция авторизации врача
адрес : /check, method POST.
Принимает параметры:
log - имя пользователя
pass - пароль - в MD5

Возвращает результат типа:
{'answer': 1, 'Error': [], 'info_key': {'Doctor_id': 3, 'my_key': '8c550a44e79e4488a45b5ce3fe5efe59'}, 'info_user': {'id': 3, 'Username': 'user2', 'Doctor': 1, 'Admin': 0}}
'answer' - если 1 то авторизация успешная, если ноль то авторизация не прошла.
В поле 'info_key' информация о ключе пользователя
НЕ успешная авторизация
'info_user' - информация о пользователе в том числе права доктора и права администратор
{'answer': 0, 'Error': [{'тип': 'Не пройдена авторизация', 'exeption': 'Не верный логин или пароль'}]}

