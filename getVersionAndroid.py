import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","accept-encoding":"gzip, deflate, sdch"}

r = requests.get("https://play.google.com/store/apps/details?id=venturesity.user&hl=en")

soup = BeautifulSoup(r.text.encode('utf-8'),'html.parser')
body = soup.find('div',{'class':'inner-container'})

version = body.find_all('div',{'class':'details-wrapper'})

currentVersion = float(version[3].find_all('div',{'class':'meta-info'})[3].find('div',{'class':'content'}).getText().replace(' ',''))

print currentVersion

