import time
import schedule
from hnmanager import HNManager
from twittermanager import TwitterManager

hn = HNManager()
tm = TwitterManager()

def main():
    hn.fillinterestsdata()
    fetchnews()
    schedule.every().day.at("07:00").do(fetchnews)
    schedule.every(1).hours.do(getnews)
    while True:
        schedule.run_pending()
        time.sleep(300)


def fetchnews():
    hn.fetchbestnews()


def getnews():
    news = hn.getstory()
    if news is not None:
        print("getnews :" + news)
        tm.tweet(news)
    else:
        print("Something went wrong, tweet was not created")


if __name__ == '__main__':
    main()
