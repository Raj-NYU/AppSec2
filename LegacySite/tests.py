from pydoc import text
from django.test import TestCase
import requests


class Part1Tests(TestCase):
    def test_xss_vulnerability(self):
        URL = 'http://127.0.0.1:8000/gift.html'
        session = requests.Session()
        params = {'director': '<script>alert("{alert_string}")</script>'}
        response = session.get(URL, params=params)

        if response.text.find("<script>alert\('{alert_string}'\)</script>") != -1:
            print("XSS vulnerability detected")
        else:
            print("SAFE!!!")

class TestCSRFExploit(TestCase):
    def test_csrf_exploit(self):
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