import sys
import os
from hnmanager import HNManager
from urlshortner import URLShortner


def main():
    print(URLShortner().shorten("https://www.google.com"))
    hn = HNManager()
    hn.fillinterestsdata()
    hn.fetchbestnews()


if __name__ == '__main__':
    main()
