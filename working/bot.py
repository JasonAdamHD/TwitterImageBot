#!/usr/bin/env python3

import random
import tweepy
import shutil
import json
import os
from threading import Timer

def main():
    credsFile = "./credentials.json"
    cfgFile = "./config.json"
    f = open(credsFile)
    creds = json.load(f)
    f.close()
    f = open(cfgFile)
    config = json.load(f)
    f.close()

    CONSUMER_API_KEY = creds["CONSUMER_API_KEY"]
    CONSUMER_API_KEY_SECRET = creds["CONSUMER_API_KEY_SECRET"]
    ACCESS_TOKEN = creds["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = creds["ACCESS_TOKEN_SECRET"]

    interval = config['interval']
    approved_folder = config['approved_files']
    posted_folder = config['posted_files']

    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    create_tweet(api, interval, approved_folder, posted_folder)
    
def create_tweet(api: tweepy.API, interval: int, approved_folder: str, posted_folder: str):
    #Call this func in the future
    try:
        Timer(interval, create_tweet, args=[api, interval, approved_folder, posted_folder]).start()
        #Get the random file from the approved folder
        file = random.choice(os.listdir(approved_folder))
        filepath = approved_folder + file
        #Create the tweet
        api.update_status_with_media(file, filepath)
        newFilepath = posted_folder + file
        #Move the file to the posted folder
        shutil.move(filepath, newFilepath)
        print("tweeting")
    except IndexError:
        print("error in creating the tweet")
    except:
        #TODO: Specify exception for failure to create tweet.
        #TODO: Specify exception for no files in approval folder.
        #TODO: specify final exception exceptions. 
        print("some other error")

if __name__ == '__main__':
    main()
