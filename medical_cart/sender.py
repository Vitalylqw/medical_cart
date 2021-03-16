# coding=utf-8
import hashlib
import requests

# 1
# url = 'http://188.243.56.86:7777/check_admin'
# # url = 'http://127.0.0.1:5000//check_admin'
# data = {
#         'log':'Администратор',
#         'pass':hashlib.md5("Администратор".encode('utf-8')).hexdigest()
#     }
# response = requests.post(url,data = data)
# print(response.json())
# 2
# url = 'http://188.243.56.86:7777/check_doctor'
# # url = 'http://127.0.0.1:5000/check_doctor'
# data = {
#         'log':'user2',
#         'pass':hashlib.md5("пароль".encode('utf-8')).hexdigest()
#     }
#
# response = requests.post(url,data = data)
# print(response.json())
# 3
# url = 'http://188.243.56.86:7777/list_users'
# data = { 'key':'b50ea3824101fbbb4216f731de332acb' }
#
# response = requests.get(url,params = data)
# print(response.json())

# # 4
# url = 'http://188.243.56.86:7777/insert_users'
# data = { 'key':'b50ea3824101fbbb4216f731de332acb','Username':'user3','password':'7e58d63b60197ceb55a1c487989a3720',
#          'FirstName':'Федр','MiddlName':'Алексеевич','SacondName':'Петерсон','Birthday':"01-24-1985",
# 'ProfSpacial':'Врач практолог','Doctor':1,'Admin':0,'off':0 }
#
# response = requests.put(url,params = data)
# print(response.json())

# 5
url = 'http://188.243.56.86:7777/update_users'
data = { 'key':'9933679106a83b0f0894a9f03c1ccfea',
         'FirstName':'Илья',
         'MiddlName':'Иванович',
         'SacondName':'Муромец',
         'Birthday':"1538-03-03",
         'ProfSpacial':'Богатырь',
         'Doctor':1,'Admin':1,'off':0 ,'id':1}

response = requests.patch(url,params = data)
print(response.json())

# 6
# url = 'http://188.243.56.86:7777/update_password'
# data = { 'key':'42ba8c86eb17df11078a78125a2a8331',
#          'pass':'e242f36f4f95f12966da8fa2efd59992',
#           'id':3}
#
# response = requests.patch(url,params = data)
# print(response.json())

# # 7
# url = 'http://188.243.56.86:7777/list_pacients'
# data = { 'key':'b50ea3824101fbbb4216f731de332acb' }
#
# response = requests.get(url,params = data)
# print(response.json())

#  8
# url = 'http://188.243.56.86:7777/insert_pacient'
# data = { 'key':'1887e8ba4713447201a5cf19934b0008','Doctor_id':5,'FirstName':'Илья','MiddlName':'Иванович','SacondName':'Козлов','Birthday':'1980-02-28','Sex':'M',
# 'Adres': 'Санкт Петербург, ул  Оптиков д 4','Phone':'+7958256378','Anamnes':'Глдаз маргает третий день','Diagnos':'Маргоглазка ?','PersDastaSoglasie':1,'SoglasieMed':1}
#
# response = requests.put(url,params = data)
# print(response.json())

#  9
# url = 'http://188.243.56.86:7777/update_pacient'
# data = { 'key':'1887e8ba4713447201a5cf19934b0008','Doctor_id':3,'FirstName':'Илья','MiddlName':'Иванович','SacondName':'Козлов','Birthday':'1980-02-28','Sex':'M',
# 'Adres': 'Санкт Петербург, ул  Оптиков д 4','Phone':'+7958256378','Anamnes':'Глаз моргает третий день','Diagnos':'Маргоглазка ?','PersDastaSoglasie':1,'SoglasieMed':1,'id':3}
#
# response = requests.patch(url,params = data)
# print(response.json())

# 10
# url = 'http://188.243.56.86:7777/check'
# # url = 'http://127.0.0.1:5000/check_doctor'
# data = {
#         'log':"OR 1=1",
#         'pass':"OR 1=1"
#     }
#
# response = requests.post(url,data = data)
# print(response.json())


# url = 'http://188.243.56.86:7777/insert_users'
# data = { 'key':'b50ea3824101fbbb4216f731de332acb','Username':'','password':'7e58d63b60197ceb55a1c487989a3720',
#          'FirstName':'Федр','MiddlName':'Алексеевич','SacondName':'Петерсон','Birthday':"",
# 'ProfSpacial':'Врач практолог','Doctor':1,'Admin':0,'off':0 }
#
# response = requests.put(url,params = data)
# print(response.json())