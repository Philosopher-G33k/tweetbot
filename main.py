import sys
import os
from hnmanager import HNManager


def main():
    hn = HNManager()
    hn.fillinterestsdata()
    hn.fetchbestnews()


if __name__ == '__main__':
    main()
