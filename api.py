omdb_url = 'http://www.omdbapi.com/?i=tt3896198&apikey=4aa872c2'
nyt_url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=206f825296f14c518e3d3cc35b7272a5'



import urllib2
import json

def omdb_info(title):
    try:
        global omdb_url
        #if title has a space in it
        url = omdb_url + "&t=" + title.replace(" ", "%20")
        uread = urllib2.urlopen(url).read()
        udict = json.loads(uread)
        print "hello"
        if udict['Response'] == "False":
            d = {'Director':'N/A', 'Plot':'N/A', 'Actors':'N/A', 'Poster':'http://sadcatdiary.com/wp-content/uploads/2015/07/sadcatsmall.jpg'}
            print "sometsrhing"
            return d
        return udict
    except:
        print "Error: API key was set up incorrectly! omdb"
        d = {'Director':'N/A', 'Plot':"N/A", "Actors":"N/A", 'Poster':'http://sadcatdiary.com/wp-content/uploads/2015/07/sadcatsmall.jpg'}
        return d
    
def nyt_info(title):
    try:
        global nyt_url
        url = nyt_url + "&query=" + title.replace(" ", "%20")
        uread = urllib2.urlopen(url).read()
        udict = json.loads(uread)
        if udict['num_results'] == 0:
            d = {'results':[{'link':{'url':"#", 'suggested_link_text': "N/A"}}]}
            return d
        return udict
    except:
        print "Error: API key was set up incorrectly! nyt"
        d = {'results':[{'link':{'url':"#", 'suggested_link_text': "N/A"}}]}
        return d

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
