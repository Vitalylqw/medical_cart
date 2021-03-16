import pymysql

MY_SQL_IP  = '185.219.40.60'
MY_SQL_USER = 'instrumentoz'
MY_SQL_PASS = 'aqgj~ztb48Q9'
MY_SQL_DB_TEST = 'medical'

def clos_connect(cursor_mysql,conn_mysql):
    if cursor_mysql:
        cursor_mysql.close()
    if conn_mysql:
        conn_mysql.close()

def db_conect(dict=False):
    '''Подключение к БД'''
    error = []
    dic = {}
    try:
        if dict:
            conn_mysql = pymysql.connect(MY_SQL_IP, MY_SQL_USER, MY_SQL_PASS, MY_SQL_DB_TEST,cursorclass=pymysql.cursors.DictCursor)
        else:
            conn_mysql = pymysql.connect(MY_SQL_IP, MY_SQL_USER, MY_SQL_PASS, MY_SQL_DB_TEST)
        cursor_mysql = conn_mysql.cursor()
    except Exception as E:
        print('Не удалось подключиться к базе')
        dic['type'] = 'Не удалось подключиться к базе'
        dic['exeption'] = str(E)
        error.append(dic)
        clos_connect(cursor_mysql,conn_mysql)
        return None,None,{'answer': 0, 'Error': error}
    else:
        print('Подключение к БД  удалось')
        return conn_mysql,cursor_mysql,None

def get_data(data,param):
    error = []
    dic = {}
    try:
        ins_data = [data[i] for i in param]
    except Exception as E:
        print('Не удалось извлечь данные')
        dic['type'] = 'Не удалось извлечь данные'
        dic['exeption'] = str(E)
        error.append(dic)
        return None,{'answer': 0, 'Error': error}
    else:
        return ins_data,None

def make_request(cursor_mysql,text_query,data=None):
    error = []
    dic = {}
    try:
        cursor_mysql.execute(text_query,data)
    except Exception as E:
        print('Не удалось выполнить запрос')
        dic['тип'] = 'Не удалось выполнить запрос'
        dic['exeption'] = str(E)
        error.append(dic)
        cursor_mysql.close()
        return None,{'answer': 0, 'Error': error}
    else:
        return cursor_mysql,None

def valid_users(my_key):
    '''Провека ключа на валидность по сроку'''
    conn_mysql, cursor_mysql,answer = db_conect()
    if not conn_mysql:
        return answer
    text_query = '''SELECT IF (now()>valid_until , 0,1) FROM access_keys where my_key = %s'''
    cursor_mysql, answer = make_request(cursor_mysql, text_query, data=my_key)
    res = cursor_mysql.fetchone()
    if not cursor_mysql:
        clos_connect(cursor_mysql, conn_mysql)
        return answer
    if res:
        return {'answer':res[0]}
    return {'answer':0,'error':'Не найден ключ'}