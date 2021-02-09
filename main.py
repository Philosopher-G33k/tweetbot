import sys
import os
from hnmanager import HNManager
from urlshortner import URLShortner


def main():
    print(URLShortner().shorten("https://www.google.com"))
    hn = HNManager()
    hn.fillinterestsdata()
    hn.fetchbestnews()
    news = hn.getstory()
    print(URLShortner().shorten(news.url))


if __name__ == '__main__':
    main()
