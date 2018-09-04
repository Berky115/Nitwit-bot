import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

for tweet in tweepy.Cursor(api.search, q='Search term here').items(5):
    try:
        print('\nTweet by- @' + tweet.user.screen_name)
        tweet.retweet()
        tweet.favorite()
        if not tweet.user.following:
            tweet.user.follow()
            print('Following @'+ tweet.user.screen_name)

        api.update_status("@"+str(tweet.author.screen_name) + " message goes here", in_reply_to_status_id = tweet.id)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
