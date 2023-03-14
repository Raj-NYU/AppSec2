# Bugs

## XSS Summary:
In my investigation of the website's security, I discovered an XSS exploit that utilized "safe tags" present in gift.html and item-single.html. These tags, designed to prevent code from being escaped, could be manipulated by attackers to perform an XSS attack. Specifically, an attacker could use the code: http://127.0.0.1:8000/gift.html?director=<script>alert("HACKED!!!")</script> to execute malicious code.
To address this vulnerability, I determined that the safe tags were the root cause and could actually render the contents of item-single.html and gift.html files unsafe. To mitigate this issue, I removed the safe tags from the "director" tag and conducted thorough manual tests to ensure the website's normal functionality.
In addition, I developed a comprehensive test that scans the server's response for the string "<script>alert("{alert_string}")</script>". This test effectively detects if the input was executed as JavaScript code and displays "XSS vulnerability detected" if a script is detected. Conversely, if the input was properly sanitized or escaped by the server, the test returns "SAFE!!!".
Overall, these measures will help to enhance the website's security and protect it from potential XSS attacks.


## CSRF Summary:
CSRF, or Cross-Site Request Forgery, is a security vulnerability where attackers can utilize a user's credentials on one website to perform unintended actions on another website without the user's knowledge or consent. Developers can take various measures to prevent CSRF attacks, such as utilizing CSRF tokens and SameSite cookies.

Exploit: During my analysis of the giftcard website's security, I discovered a potential CSRF vulnerability. To exploit this vulnerability, I created an HTML payload that could be placed within a malicious webpage. When the authenticated user visits the attacker's webpage, a HTTP request is triggered to the vulnerable site with the user's session token. The attacker can then perform actions as if they were the user, such as gifting a card to themselves. The malicious HTML code is included in the CSRF Payload folder for reference.

Fix: To address this vulnerability, I implemented several measures. First, I added the "@csrf_protect" tag to the gift_card_view function in the views.py file where Professor Gallagher had commented. This tag enables CSRF protection for a specific view function and generates a token that is included in the HTML form and verified on submission, preventing CSRF attacks. Without this protection, attackers can submit malicious data to the website.
Additionally, I inserted the {% csrf_token %} template tag in the gift.html file on line 78 to generate a unique CSRF token for each form submission. This token is checked against the submitted form data to ensure that they match during page loading, rejecting any requests that do not match. This measure helps to further protect the website against potential CSRF attacks.
In conclusion, these measures help to enhance the security of the giftcard website and prevent potential CSRF attacks, providing greater protection to users and their sensitive information.

## SQLi Summary:
Exploit: During my security analysis of the giftcard website, I came across a potential SQL injection vulnerability. To test this vulnerability, I created a payload called SQLi.gftcrd and submitted a giftcard through the use.html page. As a result, the website outputted the saltedhash value for the admin in PNG format.

Fix: To address this vulnerability, I made a modification to the codebase by wrapping the variable signature in brackets on line 198. This simple but effective measure helps prevent the use of special characters in the query, also known as parameterization. By parameterizing the query, special characters cannot be executed, preventing potential SQL injection attacks.
In conclusion, this fix helps to enhance the security of the giftcard website and prevent potential SQL injection attacks, providing greater protection to users and their sensitive information.

## OS Command Injection Summary:
During my analysis of the giftcard website, I discovered a potential vulnerability that involved the binary giftcardreader file. By thoroughly searching through the files, I found that the extras.py file contained the parse_card_data() function, which parsed the cards file and path after uploading. Additionally, a helpful hint from Kevin's comment led me to believe that there was a vulnerability present in this area. I then decided to review the views.py file to understand how entries are processed, which revealed the potential for an OS command injection attack.
To test this vulnerability, I created a "dummy" giftcard to input, which triggered an execution at the backend. I then performed an OS command injection attack by running "gift;ifconfig;ls; & echo HACKED!!! &". This would cause a segmentation fault, list (ls) the contents of a directory, and display a message (in this case, "HACKED!!!"), all of which would show up in the server's terminal.
To remediate this vulnerability, I identified that the main input for injecting a command to the server terminal is a semi-colon. Therefore, I added an if statement that would run a check to ensure that a semicolon was not present within a file. After making this fix, I re-ran the same exploit and confirmed that the vulnerability was no longer present.
In conclusion, my thorough analysis and remediation of this vulnerability helped to enhance the security of the giftcard website, preventing potential OS command injection attacks and providing greater protection to users and their sensitive information.

