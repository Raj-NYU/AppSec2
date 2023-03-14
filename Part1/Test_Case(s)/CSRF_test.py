import requests
import self as self

session = requests.Session()
cookies = requests.cookies.RequestsCookieJar()
URL = 'http://127.0.0.1:8000/gift/0'
data = {'username': 'hacker', 'password': 'hacker'}
session.post(URL, data=data, cookies=cookies)
body_text = session.get(URL, cookies=cookies).text

if "hacker" in body_text:
    self.fail("CSRF exploitable")
else:
    print("SAFE!!!")
