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
        url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=7e66bca8ed8d4c4a87789faec87abf66" + "&query=" + title.replace(" ", "%20")
        uread = urllib2.urlopen(url).read()
        udict = json.loads(uread)
        return udict
    except:
        print "Error: API key was set up incorrectly!"
        return -1

def tastedive_info(title):
    try:
        global tastedive_url
        url = tastedive_url + "&q=" + title.replace(" ", "%20")
        uread = urllib2.urlopen(url).read()
        udict = json.loads(uread)
        return udict
    except:
        print "Error: API key was set up incorrectly!"
        return -1
