import requests

class Part1Tests(TestCase):
    def test_xss_vulnerability(self):
        #Change URL if needed to for more tests
        URL = 'http://127.0.0.1:8000/gift.html'
        session = requests.Session()
        params = {'director': '<script>alert("{alert_string}")</script>'}
        response = session.get(URL, params=params)

        if response.text.find("<script>alert\('{alert_string}'\)</script>") != -1:
            print("XSS vulnerability detected")
        else:
            print("SAFE!!!")
