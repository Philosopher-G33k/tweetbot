from hackernews import hn
import json

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
        pass
    
    def fillinterestsdata(self):
        f = open("interests.json")
        self.interests = json.loads(f.read())["interests"]
