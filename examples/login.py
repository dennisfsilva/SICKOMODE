import requests

url = "http://quickrecipe.azurewebsites.net/api/v1/login/"

r = requests.get(url, auth=('carlos@admin.pt','12345'))

print(r.text)
