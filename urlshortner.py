import bitlyshortener

class URLShortner:
    def __init__(self):
        self.tokens_pool = ['e317bc806d59face4dfae11bf7ca6b0d2c42fd08']

    def shorten(self, url):
        shortener = bitlyshortener.Shortener(tokens=self.tokens_pool, max_cache_size=256)
        shortenedurl = shortener.shorten_urls([url])
        return shortenedurl[0]


