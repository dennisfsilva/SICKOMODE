import requests
  
url = "http://127.0.0.1:5000/api/v1/update_recipe/26"
obj = {'id_ingredients':[4,5], 'amount':[25, 5] }

r = requests.put(url, json = obj, headers = {'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyNDgwNDZ9.17dLzoXSaDgbZwYkfJKZ-mlbmCqzzfcBOaQ7zvHeFfs'})

print(r.text)
