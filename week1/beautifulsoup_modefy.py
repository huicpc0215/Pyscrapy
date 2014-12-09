from BeautifulSoup import BeautifulSoup

doc = ['<html><head><title>Page title</title></head>',
              '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
              '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
              '</html>']
soup = BeautifulSoup(''.join(doc))

titleTag=soup.html.head.title;
print titleTag
titleTag['id']='new title tag'
print titleTag
titleTag.contents[0].replaceWith("new title")
print titleTag
print soup.p.extract()
print soup.prettify()
