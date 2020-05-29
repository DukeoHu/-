import requests
import webbrowser

url1 = 'http://www.wechall.net/challenge/training/programming1/index.php?action=request'
url2 = 'http://www.wechall.net/challenge/training/programming1/index.php?answer='
r = requests.get(url1)
print(r.cookies)
c={"WC":"i_like_cookies for .wechall.net/"}
key = requests.get(url1,cookies=c)
print(key.text)
m=requests.get(url2+key.text,cookies=c)
print(m.text)
