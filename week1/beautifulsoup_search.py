from BeautifulSoup import BeautifulSoup
import re
doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print "\nsoup->"
print soup.prettify()

titleTag=soup.html.head.title
print "\nhere is titleTag"
print titleTag
print titleTag.string

print "\nhere is len(soup('p'))"
print len(soup('p'))

print "\nhere is soup.findAll('p',align=\"center\")"
print soup.findAll('p',align="center")
print soup.findAll('p',align="center")

print "\nhere is soup.find('p',align=\"center\")"
print soup.find('p',align="center")

print "\nhere is soup.find(\'p\',aligen=\"center\")[0][\'id\']"
print soup('p',align="center")[0]['id']

print "\nhere is soup(\'p\',align=re.compile(\'^b.*\'))[\'id\']"
print soup.find('p',align=re.compile('^b.*'))['id']

print "\nhere is soup.find(\'p\').b.string"
print soup.find('p').b.string

print "\nhere is soup(\'p\')[1].b.string"
print soup('p')[1].b.string
