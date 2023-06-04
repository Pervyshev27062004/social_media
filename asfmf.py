import requests


r = requests.get("http://127.0.0.1:8000/", params={"title": "test"})
print(r.content)

r = requests.get("http://127.0.0.1:8000/api/posts/")
print(r.json())

r = requests.post("http://127.0.0.1:8000/register/", data={
   "first_name": "Test",
   "last_name": "Test",
   "email": "test@test.com",
   "password": "Test",
})
print(r.status_code)
