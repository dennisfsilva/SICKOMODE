import requests
  
url = "http://127.0.0.1:5000/api/v1/beers/random"

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyMTk2NzR9.i9R5NOtKSWs_THp9XZgpPtyzzhRR1_Ks6741PK07MzE"})

print(x.text)
