import time
import schedule
from hnmanager import HNManager

hn = HNManager()

def main():
    hn.fillinterestsdata()
    # schedule.every().day.at("07:00").do(fetchnews)
    fetchnews()
    schedule.every(2).hours.do(getnews)
    while True:
        schedule.run_pending()
        time.sleep(60)


def fetchnews():
    hn.fetchbestnews()


def getnews():
    news = hn.getstory()
    print(news)


if __name__ == '__main__':
    main()
