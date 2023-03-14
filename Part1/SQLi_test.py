import requests
import self

file = open('Part1/SQLi_Payload/sqli.gftcrd')
URL = 'http://127.0.0.1:8000/use.html'
session = requests.Session()
body = session.post(URL, data=file)
card_key = ""
if body.text.find(card_key):
    self.fail("SQL Injection vulnerability detected!!!")
else:
    print("SAFE!!!")