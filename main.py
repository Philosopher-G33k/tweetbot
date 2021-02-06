import sys
import os
from hackernews import hn

def main():
    news_client = hn.NewsClient()
    print("The system info is given below:")
    print(sys.platform)
    print(os.cpu_count())
    print(str(news_client.get_best_story(fetchMax=10)[0]))



if __name__ == '__main__':
    main()
