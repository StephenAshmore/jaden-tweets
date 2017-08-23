from __future__ import unicode_literals

import tweepy #https://github.com/tweepy/tweepy

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Twitter API credentials
consumer_key='mF3lkvUjvfoDcUrpg9tQpG9PD'
consumer_secret='R1J31igqsThRQqIHsb646mufOMXbBXbEg9w9webUi1gj62MP7N'
access_token_key='2390466710-yCRTiaz2HZR7KorS7ZkydtezrGj4yfjplLIGznv'
access_token_secret='mK83i2cbAyhkm6yyAb3LRRf1ewpHuFLWp9Z0iix5RmpWX'

screen_name = 'officialjaden'

#Twitter only allows access to a users most recent 3240 tweets with this method

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

#initialize a list to hold all the tweepy Tweets
alltweets = []

#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name=screen_name, count=200)

#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
	new_tweets = api.user_timeline(screen_name=screen_name,
                                   count=200,
                                   max_id=oldest)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	print("...{} tweets downloaded so far".format(len(alltweets)))

#transform the tweepy tweets into a 2D array that will populate the csv
outtweets = [tweet.text for tweet in alltweets]

#write the csv
with open('output/jaden_tweets.txt', 'wb') as f:
    f.write('\n'.join(outtweets) + '\n')

pass
