import urllib2
import json

def omdb_info(title):
    try:
        global omdb_url
        #if title has a space in it
        url = omdb_url + "&t=" + title.replace(" ", "%20")
        uread = urllib2.urlopen(url).read()
        udict = json.loads(uread)
        return udict
    except:
        print "Error: API key was set up incorrectly!"
        return -1
    
def nyt_info(title):
    try:
        global nyt_url
        url = omdb_url + "&t=" + title.replace(" ", "%20")
        uread = urllib2.urlopen(url).read()
        udict = json.loads(uread)
        return udict
    except:
        print "Error: API key was set up incorrectly!"
        return -1

def tastedive_info(title):
    try:
        global tastedive_url
        url = tastedove_url + title.replace(" ", "%20")
        uread = urllib2.urlopen(url).read()
        udict = json.loads(uread)
        return udict
    except:
        print "Error: API key was set up incorrectly!"
        return -1
