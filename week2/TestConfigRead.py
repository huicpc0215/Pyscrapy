import ConfigParser
config=ConfigParser.RawConfigParser()
config.read('config.ini')

my_id=config.get('My_section','id')
my_passwd=config.get('My_section','passwd')
my_no_exist=config.get('My_section','no_filed')
print my_id
print my_passwd
print my_no_exist
if len(my_no_exist) == 0:
    my_no_exist=raw_input("please specify your no exist file")
    config.set('My_section','no_filed',my_no_exist)
    configfile=open('config.ini','w')
    config.write(configfile)
else :
    print "Exist!"
