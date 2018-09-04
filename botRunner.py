import tweepy
import requests
import os

from time import sleep
from credentials import *

# Set up
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#image process methods
def tweet_image_gif(message, url):
    filename = 'temp.gif'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
        print(message)
    else:
        print("Unable to download/use image")

def tweet_image_jpg(message, url):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
        print(message)
    else:
        print("Unable to download/use image")
        print(message)
        print(url)

#file Read
my_file = open('updates.txt', 'r')
file_lines = my_file.readlines()
my_file.close()

#status update
#For online image/message. use "___" in output file in order to split properly
for line in file_lines:
    try:
        if ".jpg" in line:
            data = line.split("___")
            tweet_image_jpg(data[0], data[1])
        elif ".gif" in line:
            data = line.split("___")
            tweet_image_gif(data[0], data[1])
        elif line != '\n':
            print(line)
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
#post in seconds
    sleep(3600)

# nohup python3 botRunner.py & to run in background
