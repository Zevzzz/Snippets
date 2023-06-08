
import NewsScraper as ns
import bardapi
bardapi.PAUSE = 0.00
bard = bardapi.core.Bard('XQgii_FEWOt8JLZ4VdEUN-KvSm2SejKwrnhprFhGjTUP5gxuZjm9Wv3XecD0__JZU4KXYQ.')
def getBardTitle(title, wordcount):
    while True:
        segment = ''
        try:
            text = 'Summarize the following news article title in under ' + str(wordcount) + ' words: ' + title
            text = str(bard.get_answer(text).get('content'))
            segment = text[text.index('\n\n') + 2:]
            break
        except ValueError:
            pass
    return segment.replace('*', '').replace('\n', '')
def getBardContent(content, wordcount):
    while True:
        segment = ''
        try:
            text = 'Summarize the following article to about ' + str(wordcount) + ' words: ' + content
            text = str(bard.get_answer(text).get('content'))
            segment = text[text.index('\n\n') + 2 :]
            break
        except ValueError:
            pass
    return segment.replace('*', '').replace('\n', '')



def getContent(prompt, articleCount, titleLength, contentLength):
    while True:
        try:
            news = ns.getNews(prompt, articleCount)
            titles, contents = ns.getDetails(news)

            cleanedTitles = []
            cleanedContents = []

            for i, title in enumerate(titles):
                cleanedTitles.append(getBardTitle(title, titleLength))
                cleanedContents.append(getBardContent(contents[i], contentLength))
            break
        except:
            print('News Request Error, trying again...')

    return cleanedTitles, cleanedContents





