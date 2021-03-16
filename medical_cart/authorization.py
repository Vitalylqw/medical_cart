# coding=utf-8


import global_fun as gf



def check_admin(data):
    """Проверка авторизации администратора"""
    # Попытка подключиться к БД
    error=[]
    dic = {}
    conn_mysql,cursor_mysql,answer = gf.db_conect()
    if not conn_mysql:
        return answer

    # Получим логин и пароль из пришедших данных
    ins_data,answer = gf.get_data(data,['log','pass'])
    if not ins_data:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer

    # Запрос найдеться ли пользователь м таким логином и паролем и справами админа
    text_query = '''SELECT COUNT(*) FROM users WHERE Username = %s AND password = %s AND Admin = 1 AND off = 0'''
    cursor_mysql,answer = gf.make_request(cursor_mysql,text_query,data=ins_data)
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    res = cursor_mysql.fetchone()[0]

    if res == 0:
        dic['тип'] = 'Не пройдена авторизация'
        dic['exeption'] = 'Не верный логин или пароль'
        error.append(dic)
        return   {'answer': res, 'Error': error}
    else:
        # Добавим запись о новом ключе
        text_query = '''INSERT INTO access_keys (Doctor_id,my_key) SELECT id,MD5(NOW()+id) FROM users WHERE Username = %s AND password = %s  AND Admin = 1 AND off = 0'''
        cursor_mysql, answer = gf.make_request(cursor_mysql, text_query, data=ins_data)
        if not cursor_mysql:
            gf.clos_connect(cursor_mysql, conn_mysql)
            return answer
        conn_mysql.commit()

        # Получим данные о новом ключе
        text_query = '''SELECT Doctor_id , my_key FROM access_keys ak join users u ON ak.Doctor_id = u.id WHERE u.Username = %s ORDER by ak.id DESC limit 1'''
        cursor_mysql, answer = gf.make_request(cursor_mysql, text_query, data=ins_data[0])
        if not cursor_mysql:
            gf.clos_connect(cursor_mysql, conn_mysql)
            return answer
        answer = cursor_mysql.fetchone()
        info_key={'id':answer[0],'username':ins_data[0],'kye':answer[1]}
        gf.clos_connect(cursor_mysql, conn_mysql)
        return {'answer': res, 'Error': error,'info_key':info_key}


def check_doctor(data):
    """Проверка авторизации администратора"""
    # Попытка подключиться к БД
    error=[]
    dic = {}
    conn_mysql,cursor_mysql,answer = gf.db_conect()
    if not conn_mysql:
        return answer

    # Получим логин и пароль из пришедших данных
    ins_data,answer = gf.get_data(data,['log','pass'])
    if not ins_data:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer

    # Запрос найдеться ли пользователь м таким логином и паролем и справами админа
    text_query = '''SELECT COUNT(*) FROM users WHERE Username = %s AND password = %s AND Doctor = 1 AND off = 0'''
    cursor_mysql,answer = gf.make_request(cursor_mysql,text_query,data=ins_data)
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    res = cursor_mysql.fetchone()[0]
    if res == 0:
        dic['тип'] = 'Не пройдена авторизация'
        dic['exeption'] = 'Не верный логин или пароль'
        error.append(dic)
        return   {'answer': res, 'Error': error}
    else:
        # Добавим запись о новом ключе
        text_query = '''INSERT INTO access_keys (Doctor_id,my_key) SELECT id,MD5(NOW()+id) FROM users WHERE Username = %s AND password = %s  AND Doctor = 1 AND off = 0'''
        cursor_mysql, answer = gf.make_request(cursor_mysql, text_query, data=ins_data)
        if not cursor_mysql:
            gf.clos_connect(cursor_mysql, conn_mysql)
            return answer
        conn_mysql.commit()

        # Получим данные о новом ключе
        text_query = '''SELECT Doctor_id , my_key FROM access_keys ak join users u ON ak.Doctor_id = u.id WHERE u.Username = %s ORDER by ak.id DESC limit 1'''
        cursor_mysql, answer = gf.make_request(cursor_mysql, text_query, data=ins_data[0])
        if not cursor_mysql:
            gf.clos_connect(cursor_mysql, conn_mysql)
            return answer
        answer = cursor_mysql.fetchone()
        info_key={'id':answer[0],'username':ins_data[0],'key':answer[1]}
        gf.clos_connect(cursor_mysql, conn_mysql)
        return {'answer': res, 'Error': error,'info_key':info_key}



def check(data):
    """Авторизация пользователя с выдачей прав"""
    # Попытка подключиться к БД
    error=[]
    dic = {}
    conn_mysql,cursor_mysql,answer = gf.db_conect(dict=True)
    if not conn_mysql:
        return answer

    # Получим логин и пароль из пришедших данных
    ins_data,answer = gf.get_data(data,['log','pass'])
    if not ins_data:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer

    # Запрос найдеться ли пользователь м таким логином и паролем и справами админа
    text_query = '''SELECT id, Username, Doctor, Admin FROM users WHERE Username = %s AND password = %s  AND off = 0'''
    cursor_mysql,answer = gf.make_request(cursor_mysql,text_query,data=ins_data)
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    info_user = cursor_mysql.fetchone()

    if not info_user:
        dic['тип'] = 'Не пройдена авторизация'
        dic['exeption'] = 'Не верный логин или пароль'
        error.append(dic)
        return   {'answer': 0, 'Error': error}
    else:
        # Добавим запись о новом ключе
        text_query = '''INSERT INTO access_keys (Doctor_id,my_key) SELECT id,MD5(NOW()+id) FROM users where Username = %s'''
        cursor_mysql, answer = gf.make_request(cursor_mysql, text_query,ins_data[0])
        if not cursor_mysql:
            gf.clos_connect(cursor_mysql, conn_mysql)
            return answer
        conn_mysql.commit()

        # Получим данные о новом ключе
        text_query = '''SELECT Doctor_id , my_key FROM access_keys ak join users u ON ak.Doctor_id = u.id WHERE u.Username = %s ORDER by ak.id DESC limit 1'''
        cursor_mysql, answer = gf.make_request(cursor_mysql, text_query, data=ins_data[0])
        if not cursor_mysql:
            gf.clos_connect(cursor_mysql, conn_mysql)
            return answer
        info_key = cursor_mysql.fetchone()
        gf.clos_connect(cursor_mysql, conn_mysql)
        return {'answer': 1, 'Error': error,'info_key':info_key,'info_user':info_user}


