import bitly_api

class URLShortner:
    def __init__(self):
        pass

    def shorten(self,url):
        bitly = bitly_api.Connection("ishan13", "e317bc806d59face4dfae11bf7ca6b0d2c42fd08")
        shortenedurl = bitly.shorten('http://google.com/')
        return shortenedurl
