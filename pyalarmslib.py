import urllib2
import urllib
import requests

import glob, os
import yaml
import logging
import datetime

STDOUT_ACTIVE = True

logging.basicConfig(filename='pyalarms.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def getDateTimeNow():
	return datetime.datetime.now().strftime("%Y%m%d_%H%M%S");


def log(msg):
	if(STDOUT_ACTIVE):
		print msg;
	logging.info(getDateTimeNow()+" : "+msg);


def loadConfiguration():
	with open("/home/user/projects/Python/pyalarms/pyalarms_private.yml", "r") as ymlfile:
		cfg = yaml.load(ymlfile)
		print cfg
	return cfg;

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text,token,chatid):
	
	URL = "https://api.telegram.org/bot{}/".format(token)
	url = URL + "sendMessage?text={}&chat_id={}".format(text, chatid)
	log("Send notifications: "+text)
	print get_url(url)



def loadPlugins():
	os.chdir("plugins")
	
	print "Load plugins..."
	res = []
	for file in glob.glob("*.py"):
		if( "__init__" not in file):
			print(file)
			res.append( str(file).split(".")[0] )
	print "Plugin Loaded: "+str(res)
	return res;
