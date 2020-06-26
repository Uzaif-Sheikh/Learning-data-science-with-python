#WE are using here urllib
from urllib.request import urlopen
url = "https://github.com/programmingwithuzaif"
file = urlopen(url)
print(file.read())         #THIS will display the HTML content of the webpage

#WE will use bs4 if you don't have bs4 do pip install bs4

from bs4 import BeautifulSoup
page="https://github.com/programmingwithuzaif"
soup = BeautifulSoup(page)
print(soup.title)
print(soup.title.string)

#JSON 

import json
d = {'1':'abc','2':'sushi'}
str = json.dumps(d)
s=json.loads(str)
print(s['1'])
