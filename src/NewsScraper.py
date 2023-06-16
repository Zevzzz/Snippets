
from gnews import GNews
from newspaper import Article

gnews = GNews()
print('News API - Online')

def getDetails(news):
    titles = [singleNews['title'] for singleNews in news]
    urls = [singleNews['url'] for singleNews in news]
    contents = []
    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        contents.append(article.text)

    return titles, contents

def getNews(topic = None, max_results = 10):
    gnews.max_results = max_results
    gnews.period = '7d'
    if topic:
        return gnews.get_news_by_topic(topic)
    else:
        return gnews.get_top_news()

def getNewsTopics(topicList):
    news = []
    for topicSet in topicList:
        news.append(getNews(topicSet[0], topicSet[1]))
    return news









