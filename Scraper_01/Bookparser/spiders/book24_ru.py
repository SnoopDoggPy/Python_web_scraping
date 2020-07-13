import scrapy
from scrapy.http import HtmlResponse
from Bookparser.items import BookparserItem


class Book24RuSpider(scrapy.Spider):
    name = 'book24_ru'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/search/?q=python']

    def parse(self, response:HtmlResponse):
        next_page = response.css('a.catalog-pagination__item::attr(href)').extract_first()
        book_links = response.css('a.book__title-link::attr(href)').extract()

        print('book24_ru', len(book_links))

        for link in book_links:
            yield response.follow(link, callback=self.book_parse)

        yield response.follow(next_page, callback=self.parse)

        pass


    def book_parse(self, response:HtmlResponse):
        id_p = response.url
        href_p = response.url
        name_p = response.css('h1.item-detail__title::text').extract_first()
        author_p = response.css('a.item-tab__chars-link::text').extract_first()
        price_new_p = response.css('div.item-actions__price b::text').extract_first()
        price_old_p = response.css('div.item-actions__price-old::text').extract_first()
        rate_p = response.css('span.rating__rate-value::text').extract_first()
        yield BookparserItem(_id=id_p, href=href_p, name=name_p, author=author_p, price_new=price_new_p, price_old=price_old_p, rate=rate_p)
