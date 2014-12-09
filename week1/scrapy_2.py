import urllib2
request=urllib2.Request("http://jecvay.com/")
response=urllib2.urlopen(request)
page_html=response.read()
f=open("data2.txt",'w')
f.write(page_html)
