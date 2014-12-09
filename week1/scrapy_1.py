#encoding:UTF-8
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://jecvay.com/"
data = urllib2.urlopen(url).read()
data = data.decode('UTF-8')
f = open("data.txt",'w')
f.write(data)

print(data)
