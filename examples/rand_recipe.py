import requests

url = "http://quickrecipe.azurewebsites.net/api/v1/rand_recipes/"

x = requests.get(url, headers={'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAxMjExNzl9.WqAnIxKe4KwEWIUTjh1CoV7oV3g2uo86R05T8GFwLTg'})

print(x.text)
