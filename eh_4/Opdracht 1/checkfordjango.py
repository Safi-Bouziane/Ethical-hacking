import requests
import sys

url = sys.argv[1]

r = requests.get("https://www.djangosites.org/search/?query=" + url)
htmltext = r.text
if "No Sites Found!" not in htmltext:
    print("Found on djangosites.com")


r = requests.get( url + "/admin")
htmltext = r.text

if htmltext.__contains__("Log in | Django site admin"):
    print("default admin page found")
