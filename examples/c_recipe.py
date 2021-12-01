import requests

url = "http://127.0.0.1:5000/api/v1/create_recipe/"
obj = {'title': 'travis scott', 'instructions': 'astroworld is lit', 'id':[4,5,2], 'amount':[12,28,5]}

r = requests.post(url, json = obj, headers = {'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyNDgwNDZ9.17dLzoXSaDgbZwYkfJKZ-mlbmCqzzfcBOaQ7zvHeFfs'})

print(r.text)
