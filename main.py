import sys
import os
from hnmanager import HNManager



def main():
    hn = HNManager()
    hn.fillinterestsdata()
    hn.fetchbestnews()
    news = hn.getstory()
    print(news)


if __name__ == '__main__':
    main()
