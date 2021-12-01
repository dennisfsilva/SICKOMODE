import requests

url = 'http://quickrecipe.azurewebsites.net/api/v1/auth/'
obj = {'name':'Duarte Silva', 'password': '246810', 'email':'duarte@admin.pt', 'user_type':'colab'}

x = requests.post(url, json = obj)

print(x.text)
