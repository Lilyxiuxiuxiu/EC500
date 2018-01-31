#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import wget

#Twitter API credentials
consumer_key = 
consumer_secret = 
access_key = 
access_secret =




def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
       
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print ("Writing tweet objects to JSON please wait...")
    media_files = set()
    for status in alltweets:
        #json.dump(status._json,file,sort_keys = True,indent = 4)
        #try:
        #    print status.entities["media"][0]["media_url"]

        #except (NameError, KeyError):
        #    pass
#        else:
        # we have the media url
#            print json.dumps(status.entities["media"][0]["media_url"])
    #close the file
    # Jan 29th
        media = status.entities.get('media',[])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])

    print ("Done")
    file.close()

    i = 0
    for media_file in media_files:
        print (i+1)
        wget.download(media_file, str(i+1)+'.jpg')
        i=i+1




if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@Ibra_official")
