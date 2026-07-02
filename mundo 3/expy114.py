import requests
try:
    requests.get('https://pudim.com.br/')
    print('Consegui acessar site PUDIM')
except:
    print('NAO CONSEGUI ACESSAR SITE PUDIM')