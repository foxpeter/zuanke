import re

import requests
from bs4 import BeautifulSoup

url="http://www.zuanke8.com/forum.php?mod=forumdisplay&fid=15&filter=author&orderby=dateline"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400'}
html=requests.get(url,headers=headers,verify=False).text
bsObj = BeautifulSoup(html)
thradTable = bsObj.findAll("tbody",attrs={"id":re.compile(r"normalthread\w?")})

print thradTable[0]
