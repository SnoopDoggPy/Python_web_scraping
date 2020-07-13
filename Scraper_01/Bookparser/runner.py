from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Bookparser import settings
from Bookparser.spiders.labirint_ru import LabirintRuSpider
from Bookparser.spiders.book24_ru import Book24RuSpider

if __name__ == '__main__':

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    #process.crawl(LabirintRuSpider)
    process.crawl(Book24RuSpider)

    process.start()