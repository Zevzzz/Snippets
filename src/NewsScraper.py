
from gnews import GNews
from newspaper import Article

gnews = GNews()
print('News API - Online')

def getNews(topic = None, max_results = 10):
    gnews.max_results = max_results
    if topic:
        return gnews.get_news(topic)
    else:
        return gnews.get_top_news()

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










