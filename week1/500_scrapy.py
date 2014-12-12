import urllib2
import sys
import re
import datetime
from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding('UTF-8')
#header = {
#    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
#}
base_url="http://trade.500.com/jczq/?date="
base_pro="http://trade.500.com/static/public/jczq/xml/hisdata/"
#2014/1204/odds.xml
#data=urllib2.urlopen(url).read();
#data=data.decode('GBK');

tr_zid_exg=re.compile("\S+")
#soup = BeautifulSoup(''.join(data))
#trdata=soup.findAll('tr',attrs={'zid':tr_zip_exg})

f=file("data.txt",'w')
tmpDate=datetime.date(2014,12,4)
oneDay=datetime.timedelta(days=1)
#lastDay=datetime.date.today()-oneDay
lastDay=tmpDate+oneDay
db_rex=re.compile("[-+]?\d+(?:\.\d+)?")
score_rex=re.compile("^(?P<home_score>\d+):(?P<away_score>\d+)$")
while tmpDate < lastDay:
    print tmpDate
    now_url=base_url+tmpDate.strftime("%Y-%m-%d")
    now_pro=base_pro+tmpDate.strftime("%Y/%m%d/odds.xml")
    #get data soup
    #req=urllib2.Request(url=now_url,headers=header)
    print now_url
    data=urllib2.urlopen(now_url).read().decode('GBK')
    data_soup=BeautifulSoup(''.join(data))
    #get probility soup
    data=urllib2.urlopen(now_pro).read()
    pro_soup=BeautifulSoup(''.join(data))
    data=data_soup.findAll('tr',attrs={'zid':tr_zid_exg})
    for match in data:
        out=tmpDate.strftime("%Y-%m-%d")
        zid=match.get('zid');
        #print zid
        print match.get('lg')
        out=out+"\t"+match.get('lg')+"\t"+match.get('homesxname')+"\t"+match.get('awaysxname')
        #pro=pro_soup.find('match',attrs={'id':zid}).find('gl').get('avg')
        #div=match.findAll('td',attrs={'class':"oupei"})
        #for i in range( len(div) ):
        #    print div[i]
        #    if i==1 :
        #        continue
        #    else :
        #        span = div[i].findAll('span')
        #        for span_element in span :
        #            print i,span_element
        now_match=pro_soup.find('match',attrs={'id':zid})
        sp_string=now_match.find('europe').get('avg')
        pro_string=now_match.find('gl').get('avg')
        sp=db_rex.findall(sp_string)
        pro=db_rex.findall(pro_string)
        print "sp="
        print sp
        print "pro="
        print pro
        if sp and pro :
            #print "hereis===sp"
            #for sp in db_rex.finditer(sp_string):
            #    print sp
            #print "hereis===pro"
            #for pro in db_rex.finditer(pro_string):
            #    print pro
            print "has OK!"

            #print len(result0)
            for i in range ( len ( sp ) ) :
                print i,sp[i]
                out = out + "\t" + sp[i]
            for i in range ( len (pro ) ) :
                out = out + "\t" + pro[i]
        else :
            continue
        print out
        result=score_rex.search(match.find('a',attrs={'class':"score"}).text)
        if result :
            away_score=result.group("away_score")
            home_score=result.group("home_score")
            print "score"
            print away_score+" vs "+home_score
        else :
            continue
        if away_score < home_score :
            print "win!"
            out = out + "\twin"
        elif away_score == home_score :
            print "draw!"
            out = out + "\tdraw"
        else :
            print "lose!"
            out = out + "\tlose"

        #print result
        #out = out +"\t"+result
        f.write(out+"\n")
    tmpDate = tmpDate + oneDay



        #print pro



        #f.write(out)


#allzid=""
#first=True
#for trelement in trdata:
#    zid = trelement.get('zid')
#    print zid
#    if first :
#        allzid=allzid+zid
#    else:
#        allzid=allzid+","+zid
#    first=False
#f.write(allzid)
