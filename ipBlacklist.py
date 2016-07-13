#! /usr/bin/python

import json
import twitter
import os

#ACCESS_TOKEN = 'YOUR ACCESS TOKEN"'
#ACCESS_SECRET = 'YOUR ACCESS TOKEN SECRET'
#CONSUMER_KEY = 'YOUR API KEY'
#CONSUMER_SECRET = 'ENTER YOUR API SECRET'

ACCESS_TOKEN = '1340878182-KI2sFw62wY48xO0e7FSOfEmVZIpRR3K3GkclOt5'
ACCESS_SECRET = 'Hgb3R9JSHccpdY7o6Bz584YGvBjdEt22yRF42W9QfOgyf'
CONSUMER_KEY = 'fFtZTAQiVoVAocgDrHugw3br7'
CONSUMER_SECRET = 'CJXxit24UlnsnHfZDzNKd4h1TgO5WgvkOVxgcV3hTfST5Mzuxj'

# tweet format q=from%3Anetmenaces%20since%3A2016-05-01&src=typd
#tweets = ['@dh4wk']

users = ["@netmenaces","@EvilAFoot"]
susers = ["netmenaces","EvilAFoot"]


api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
# Uncomment the below two lines to check your credentials are working
#st = api.GetUserTimeline("@netmenaces")
#print ([s.text for s in st])


def createBlackList():
    with open('C:\Users\Vishnu\Desktop\My Scripts and tools\honeypot.txt', 'w') as f:
        for u in users:
            us = str(u)
            tw = api.GetUserTimeline(us)
            f.write([s.text for s in tw])
            f.write('\n')
    f.close()

def searchTweets():
    with open('C:\Users\Vishnu\Desktop\My Scripts and tools\honeypot.txt', 'a') as f:
        for name in users:
            print name
            searchQuery = "q=from%3A"+name+"%20since%3A2016-05-01&src=typd"
            searchResult = api.GetSearch(raw_query=searchQuery)
            f.write(searchResult)
            f.write('\n')
    f.close()

        
if __name__ == '__main__':
    try:
        createBlackList()
    except Exception, e:
        print(e)

    try:
        searchTweets()
    except Exception, e:
        print(e)

        


