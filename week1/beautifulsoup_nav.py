from BeautifulSoup import BeautifulSoup

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print soup.prettify()
print "\nsoup.contents[0].name"
print "->"+soup.contents[0].name

print "\nhere is contents[0].contents[0].name "
print "->"+soup.contents[0].contents[0].name

head = soup.contents[0].contents[0]
print "\nhere is head.parent.name"
print "->"+head.parent.name

print "\nhere is head.next"
print head.next

print "\nhere is head.nextSibling.name"
print head.nextSibling.name

print "\nhere is head.nextSibling.contents[0]"
print head.nextSibling.contents[0]

print "\nhere is head.nextSibling.contents[0].nextSibling"
print head.nextSibling.contents[0].nextSibling
