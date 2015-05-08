import urllib2
import cookielib
import urllib
import sys
from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding('UTF-8')
base_url="http://ctf8.simplexue.com/jia/"
requese_url="http://ctf8.simplexue.com/jia/index.php?action=check_pass"
cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
data=urllib2.urlopen(base_url)
data_soup=BeautifulSoup(''.join(data))
data=data_soup.find('div',attrs={'name':'my_expr'}).contents
now=' '.join(data[0].string.split())
now=now.replace("x","*")
result=eval(now)
loginparams = {'pass_key':result}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'};
req=urllib2.Request(requese_url,urllib.urlencode(loginparams),headers=headers)
response = urllib2.urlopen(req)
print response
thePage = response.read()
print thePage
