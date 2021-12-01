import requests
  
url = "http://quickrecipe.azurewebsites.net/api/v1/ingredient_details/3"
# obj = {'lite': 1}

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyOTgyNDd9.ShahVCl8N0yQXxqrD0OXEYcLKOZ2UgGhqO1UvfOUyWg"})

print(x.text)
