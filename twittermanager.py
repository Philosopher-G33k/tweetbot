import os
import tweepy
from dotenv import load_dotenv

class TwitterManager:
    def __init__(self):
        load_dotenv()
        auth = tweepy.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
        auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
        self.api = tweepy.API(auth)


    def reauthenticate(self):
        load_dotenv()
        auth = tweepy.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
        auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
        self.api = tweepy.API(auth)


    def tweet(self, content):
        print("=============")
        print(content)
        print("tweet method called")
        # test authentication
        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
            self.reauthenticate()
        finally:
            self.api.update_status(content)



