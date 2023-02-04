import feedparser

rss_url = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
rss = feedparser.parse(rss_url)
print(rss)
