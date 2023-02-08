import feedparser

rss_url = input(
    'Please enter the url for the rss feed that you would like to see:')

# https: // timesofindia.indiatimes.com/rssfeedstopstories.cms

def feed(rss):
    rss = feedparser.parse(rss)
    print('Here is your RSS feed:')
    print('Title: ' + rss.feed.title)
    print('Link: ' + rss.feed.link)
    print('Description: ' + rss.feed.description)


feed(rss_url)
