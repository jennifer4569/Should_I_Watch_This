
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
            d = {'Director':'N/A', 'Plot':'N/A', 'Actors':'N/A', 'Poster':'http://sadcatdiary.com/wp-content/uploads/2015/07/sadcatsmall.jpg', 'imdbRating':-1}
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
        print 'beginning'
        url = tastedive_url + "&callback&q=" + title.replace(" ", "%20")
        print url
        #url = 'https://tastedive.com/api/similar?k=290651-Ibnul-FSIX5D63&q=ergsfd'
        #uread = urllib2.urlopen(url).read()
        #uread = urllib2.urlopen(urllib2.Request(url)).read()

        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        response = opener.open(url)
        uread = response.read()
        
        print 'urlreader'
        udict = json.loads(uread)
        print 'json'
        return udict
    except:
        print "Error: API key was set up incorrectly! tastedive"
        return -1
