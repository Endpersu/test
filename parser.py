from bs4 import BeautifulSoup
from loguru import logger
import requests


class Parser:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.chapter = 1
        self.chapters = {}

    def get_novel(self):
        pass

    def get_webpage(self, link):
        response = requests.get(link)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            logger.info(f"page {link} is got")
            return BeautifulSoup(response.text, "html.parser")
        else:
            logger.error(f"page {link} is not got {response.status_code}")
