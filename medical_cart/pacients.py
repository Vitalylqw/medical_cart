# coding=utf-8

import global_fun as gf

def get_list_pacients(data):
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
    conn_mysql, cursor_mysql, answer = gf.db_conect(dict = True)
    if not conn_mysql:
        return answer
    # Получим запрос со списком пользователей
    text_query = '''SELECT id,Doctor_id, FirstName, MiddlName, SacondName, date_format(Birthday,'%Y-%m-%d') as Birthday,Sex,
Adres, Phone, Anamnes, Diagnos,PersDastaSoglasie,SoglasieMed,date_format(created_at,'%m-%d-%Y') as created_at , date_format(updated_at ,'%m-%d-%Y') as updated_at FROM pacient '''
    cursor_mysql, answer = gf.make_request(cursor_mysql, text_query)
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    res = cursor_mysql.fetchall()
    return {'answer':1,'data':res}


def insert_pacient(data):
    # Получим переданный параметр
    ins_data, answer = gf.get_data(data, ['key','Doctor_id','FirstName','MiddlName','SacondName','Birthday','Sex',
'Adres','Phone','Anamnes','Diagnos','PersDastaSoglasie','SoglasieMed'])
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
    text_query = '''INSERT INTO pacient ( Doctor_id, FirstName, MiddlName, SacondName, Birthday,Sex,
Adres, Phone, Anamnes, Diagnos,PersDastaSoglasie,SoglasieMed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor_mysql, answer = gf.make_request(cursor_mysql, text_query,data = ins_data[1:])
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    conn_mysql.commit()
    return {'answer':1}

def update_pacient(data):
    # Получим переданный параметр
    ins_data, answer = gf.get_data(data, ['key','Doctor_id','FirstName','MiddlName','SacondName','Birthday','Sex',
'Adres','Phone','Anamnes','Diagnos','PersDastaSoglasie','SoglasieMed','id'])
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
    text_query = '''UPDATE pacient SET Doctor_id = %s, FirstName = %s, MiddlName = %s, SacondName =%s,Birthday = %s,Sex = %s, Adres = %s, Phone = %s,  Anamnes= %s,  Diagnos= %s,  PersDastaSoglasie= %s, SoglasieMed = %s    WHERE id = %s'''
    cursor_mysql, answer = gf.make_request(cursor_mysql, text_query,data = ins_data[1:])
    if not cursor_mysql:
        gf.clos_connect(cursor_mysql, conn_mysql)
        return answer
    conn_mysql.commit()
    return {'answer':1}