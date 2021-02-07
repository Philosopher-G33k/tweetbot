from hackernews import hn
import json

class HNManager:
    def __init__(self):
        self.bestnews = []
        self.interests = []
        self.news_client = hn.NewsClient()

    def filterstories(self, story):
        for interest in self.interests:
            if interest.lower() in story.title.lower():
                return True
        return False

    def fetchbestnews(self):
        storylist = self.news_client.get_best_story(fetchMax=500)
        self.bestnews = list(filter(self.filterstories, storylist))

    def fillinterestsdata(self):
        f = open("interests.json")
        self.interests = json.loads(f.read())["interests"]
