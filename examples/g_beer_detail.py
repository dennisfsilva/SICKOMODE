import requests
  
url = "http://127.0.0.1:5000/api/v1/beers/12"

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyNDgwNDZ9.17dLzoXSaDgbZwYkfJKZ-mlbmCqzzfcBOaQ7zvHeFfs"})

print(x.text)
