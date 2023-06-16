
# import NewsScraper as nsfrom gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywordsimport nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')


# WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH
from sumy.summarizers.lsa import LsaSummarizer
summarizer_lsa = LsaSummarizer()

# Summarize using sumy LSA
George Floyd’s killing capped years of violence, discrimination by police
summary =summarizer_lsa("Donson was found dead shoved in a locker by percy and his bot.",30)
lsa_summary=""
for sentence in summary:
    lsa_summary+=str(sentence)
print(lsa_summary)content = "this is a very long sentence with a lot of redundant words that can be removed right now"summ_per = summarize(content, word_count = "10")
print(summ_per)def shortenTitle(titleStr, wordCount):
    tokens = word_tokenize(titleStr)
    stopWords = set(stopwords.words('english'))
    filteredTokens = [token for token in tokens if token.lower() not in stopWords]
    shortenedTokens = filteredTokens[:wordCount]
    shortenedTitle = ' '.join(shortenedTokens)
    return shortenedTitle

print(shortenTitle('This is a long sentance with lots of many redun'))

