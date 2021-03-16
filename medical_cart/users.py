# coding=utf-8

import global_fun as gf

def get_list_users(data):
    # Получим переданный параметр
    ins_data, answer = gf.get_data(data,['key'])
    if not ins_data:
        return answer
    # Проверим валидный ли ключ
    a = gf.valid_users(ins_data[0])
    if a['answer'] == 0:
        a['comment'] = 'Не удалось подтвердить действие ключа'
        return a
    # Подключимся к БД
    conn_mysql, cursor_mysql, answer = gf.db_conect(dict=True)
    if not conn_mysql:
        return answer
    # Получим запрос со списком пользователей
    text_query = '''SELECT id,Username,FirstName,MiddlName,SacondName,date_format(Birthday,'%Y-%m-%d') as Birthday,ProfSpacial,Doctor,Admin,off,date_format(created_at,'%m-%d-%Y') as created_at, date_format(updated_at,'%m-%d-%Y') as updated_at FROM users'''
    cursor_mysql, answer = gf.make_request(cursor_mysql, text_query)
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    res = cursor_mysql.fetchall()
    return {'answer':1,'data':res}

def insert_users(data):
    # Получим переданный параметр
    ins_data, answer = gf.get_data(data, ['key','Username','password','FirstName','MiddlName','SacondName','Birthday',
'ProfSpacial','Doctor','Admin','off'])
    if not ins_data:
        return answer
    # Проверим валидный ли ключ
    a = gf.valid_users(ins_data[0])
    if a['answer'] == 0:
        a['comment'] = 'Не удалось подтвердить действие ключа'
        return a
    # Подключимся к БД
    conn_mysql, cursor_mysql, answer = gf.db_conect()
    if not conn_mysql:
        return answer
    text_query = '''INSERT INTO users ( Username, password, FirstName, MiddlName, SacondName, Birthday,
ProfSpacial, Doctor, Admin, off) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor_mysql, answer = gf.make_request(cursor_mysql, text_query,data = ins_data[1:])
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    conn_mysql.commit()
    return {'answer':1}


def update_users(data):
    # Получим переданный параметр
    ins_data, answer = gf.get_data(data, ['key','FirstName','MiddlName','SacondName','Birthday',
'ProfSpacial','Doctor','Admin','off','id'])
    if not ins_data:
        return answer
    # Проверим валидный ли ключ
    a = gf.valid_users(ins_data[0])
    if a['answer'] == 0:
        a['comment'] = 'Не удалось подтвердить действие ключа'
        return a
    # Подключимся к БД
    conn_mysql, cursor_mysql, answer = gf.db_conect()
    if not conn_mysql:
        return answer
    text_query = '''UPDATE users SET FirstName = %s, MiddlName = %s, SacondName = %s, Birthday =%s,ProfSpacial = %s,Doctor = %s, Admin = %s, off = %s WHERE id = %s'''
    cursor_mysql, answer = gf.make_request(cursor_mysql, text_query,data = ins_data[1:])
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    conn_mysql.commit()
    return {'answer':1}

def update_password(data):
    # Получим переданный параметр
    ins_data, answer = gf.get_data(data, ['key','pass','id'])
    if not ins_data:
        return answer
    # Проверим валидный ли ключ
    a = gf.valid_users(ins_data[0])
    if a['answer'] == 0:
        a['comment'] = 'Не удалось подтвердить действие ключа'
        return a
    # Подключимся к БД
    conn_mysql, cursor_mysql, answer = gf.db_conect()
    if not conn_mysql:
        return answer
    text_query = '''UPDATE users SET password = %s WHERE id = %s'''
    cursor_mysql, answer = gf.make_request(cursor_mysql, text_query,data = ins_data[1:])
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    conn_mysql.commit()
    return {'answer':1}
