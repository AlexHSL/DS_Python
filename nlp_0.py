import nltk
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html, "html5lib")
# 这需要安装html5lib模块
text = soup.get_text(strip=True)
# text = text.encode("GBK", "ignore")
tokens = text.split()
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if token not in sr:
        clean_tokens.append(token)
freq = nltk.FreqDist(clean_tokens)
# for key, val in freq.items():
#     print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)
