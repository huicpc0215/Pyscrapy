import ConfigParser
config=ConfigParser.RawConfigParser()

config.add_section('My_section')
config.set('My_section','id','No_id_specify')
config.set('My_section','passwd','My_passwd')

configfile=open('config.ini','w')

config.write(configfile)
print config
