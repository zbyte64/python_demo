import aiohttp
from collections import defaultdict
import asyncio
import async_timeout
from asyncio import Semaphore
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"

HOST_SEMAPHORE = defaultdict(Semaphore)

def summerize(text):
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    return '\n'.join([str(s) for s in summarizer(parser.document, 3)])

async def fetch(session, url):
    '''
    async fetch with timeout and host semaphore
    '''
    hostname = urlparse(url).hostname
    try:
        HOST_SEMAPHORE[hostname].acquire()
        with async_timeout.timeout(10):
            async with session.get(url) as response:
                return await response.text()
    finally:
        HOST_SEMAPHORE[hostname].release()

async def wiki_lookup(topic):
    async with aiohttp.ClientSession() as session:
        url = 'http://en.wikipedia.org/wiki/%s' % topic
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'lxml')
        return soup.select('#content')[0].text

async def wiki_summerize(topic):
    text = await wiki_lookup(topic)
    return summerize(text)

async def main():
    import sys

    async def print_topic(topic):
        topic_summary = await wiki_summerize(topic)
        print(topic, ":\n", topic_summary)

    coroutines = map(print_topic, sys.argv[1:])
    await asyncio.gather(*coroutines)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
