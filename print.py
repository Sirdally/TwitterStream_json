import urllib
import json
import sys

tweet_file = open(sys.argv[1]) 
pyresponse = json.load(tweet_file)

#print type(pyresponse[u'search_metadata'])

#print pyresponse[u'search_metadata'].keys()

#print type(pyresponse[u'statuses'][0])
#print type(pyresponse[u'statuses'][0])
#print pyresponse[u'statuses'][0].keys()


print pyresponse[u'statuses'][1]['text']
