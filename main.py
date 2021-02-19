import time
import schedule
from hnmanager import HNManager
from twittermanager import TwitterManager

hn = HNManager()
tm = TwitterManager()

def main():
    hn.fillinterestsdata()
    # schedule.every().day.at("07:00").do(fetchnews)
    fetchnews()
    schedule.every(1).minutes.do(getnews)
    while True:
        schedule.run_pending()
        time.sleep(60)


def fetchnews():
    hn.fetchbestnews()


def getnews():
    news = hn.getstory()
    print("getnews :" + news)
    tm.tweet(news)


if __name__ == '__main__':
    main()
