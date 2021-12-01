import requests

url = "http://127.0.0.1:5000/api/v1/delete_ingredient/3"

x = requests.delete(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyOTY3NDl9.Nm7AyPidRfKbG3qskBAALc7BdNcJJgBbUGc-4o0nHmY"})

print(x.text)
