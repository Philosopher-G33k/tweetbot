from hackernews import hn
import json
import random
from urlshortner import URLShortner

class HNManager:
    def __init__(self):
        self.bestnews = []
        self.interests = []
        self.news_client = hn.NewsClient()
        self.previousshownnews = []

    def filterstories(self, story):
        for interest in self.interests:
            if interest.lower() in story.title.lower():
                print("story : accepted: " + story.title)
                return True
        return False

    def fetchbestnews(self):
        self.previousshownnews.clear()
        self.bestnews.clear()
        storylist = self.news_client.get_best_story(fetchMax=500)
        self.bestnews = list(filter(self.filterstories, storylist))

    def getstory(self):
        # Get length of list
        # Generate random number based on length of
        rand = random.randint(0, len(self.bestnews)-1)
        print("Total news : ")
        print(self.bestnews)
        print(len(self.bestnews))
        if rand not in self.previousshownnews:
            try:
                tweet = self.bestnews[rand].title
                url = URLShortner().shorten(self.bestnews[rand].url)
            except:
                self.getstory()
            tweet = tweet + "\n" + url
            for interest in self.interests:
                if interest.lower() in self.bestnews[rand].title.lower():
                    tweet = tweet + " #" + interest

            tweet = tweet + " #programmer #developer #geek"
            self.previousshownnews.append(rand)
            print("random index : ")
            print(rand)
            return tweet
        else:
            self.getstory()
    
    def fillinterestsdata(self):
        f = open("interests.json")
        self.interests = json.loads(f.read())["interests"]
