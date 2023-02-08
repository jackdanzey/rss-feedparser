import feedparser

rss_url = input(
    'Please enter the url for the rss feed that you would like to see:')


def feed(rss):
    rss = feedparser.parse(rss)
    print('Here is your RSS feed:')
    print('Title: ' + rss.feed.title)
    print('Link: ' + rss.feed.link)
    print('Description: ' + rss.feed.description)
    print('-----------End of feed-------------')


feed(rss_url)
