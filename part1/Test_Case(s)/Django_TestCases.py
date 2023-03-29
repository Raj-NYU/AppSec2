from django.test import TestCase, Client
import requests

# XSS
class Part1Tests(TestCase):
    def test_xss_vulnerability(self):
        client = Client()
        alert_string = "alert_string"
        response = client.get('/gift.html?director=<script>alert("{0}")</script>'.format(alert_string))
        self.assertNotContains(response, alert_string)

# CSRF
class TestCSRFExploit(TestCase):
    def test_csrf_exploit(self):
        client = Client(enforce_csrf_checks=True)
        response = client.post('/gift/0', {'username': 'hacker', 'password': 'hacker'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 403)

# SQLi
class SQLInjectionTest(TestCase):
    def test_sql_injection(self):
        client = Client()
        card_key = ""
        with open('part1/Attack_Cases/sqli.gftcrd', 'r') as file:
            response = client.post('/use.html', {'file': file})
            self.assertNotContains(response, card_key)

# OS Command Injection
class CommandInjectionTestCase(TestCase):
    def test_command_injection(self):
        client = Client()
        malicious_command = "gift;ifconfig;ls;"
        card_key = ""
        with open('part1/Attack_Cases/dummy.gftcrd', 'r') as file:
            response = client.post('/use.html', {'file': file, 'command': malicious_command})
            self.assertNotContains(response, card_key)
