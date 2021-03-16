# coding=utf-8
from flask import Flask
from flask import request
from datetime import datetime
import json
from flask_cors import CORS
import authorization as auth
import users as us
import pacients as pc


app = Flask(__name__)
ser_name = "API hospital RAN"
CORS(app)

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response



@app.route("/")
def hello():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Добро пожаловать на   сервер {ser_name}  <br> {timestamp}"

@app.route("/check",methods=['POST'])
def check():
    """Проверка авторизации любого пользователя с правами"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = auth.check(data)
    return json.dumps(res)


@app.route("/check_admin",methods=['POST'])
def check_admin():
    """Проверка авторизации администратора"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = auth.check_admin(data)
    return json.dumps(res)

@app.route("/check_doctor",methods=['POST'])
def check_doctor():
    """Проверка авторизации врача"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = auth.check_doctor(data)
    return json.dumps(res)

@app.route("/list_users",methods=['GET'])
def list_users():
    """Возвращает список пользователей"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = us.get_list_users(data)
    return json.dumps(res)

@app.route("/insert_users",methods=['PUT'])
def insert_users():
    """Добавляем нового пользователя"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = us.insert_users(data)
    return json.dumps(res)



@app.route("/update_users",methods=['PATCH'])
def update_users():
    """Изменяем пользователя"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = us.update_users(data)
    return json.dumps(res)

@app.route("/update_password",methods=['PATCH'])
def update_password():
    """Изменяем пароль пользователя"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = us.update_password(data)
    return json.dumps(res)


@app.route("/list_pacients",methods=['GET'])
def list_pacients():
    """Возвращает список анкет пациентов"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = pc.get_list_pacients(data)
    return json.dumps(res)


@app.route("/insert_pacient",methods=['PUT'])
def insert_pacient():
    """Заносит в БД новую  анкету  пациента"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = pc.insert_pacient(data)
    return json.dumps(res)

@app.route("/update_pacient",methods=['PATCH'])
def update_pacient():
    """Заносит в БД новую  анкету  пациента"""
    error = []
    dic = {}
    try:
        data = request.values
    except Exception as E:
        dic['Тип'] = 'Не удалось получить параметры'
        dic['exeption'] = str(E)
        error.append(dic)
        res = {'answer':0,'Error':error}
        return json.dumps(res)
    res = pc.update_pacient(data)
    return json.dumps(res)

# app.run('')
app.run('192.168.1.64')
