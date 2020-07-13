import scrapy
from scrapy.http import HtmlResponse
from Bookparser.items import BookparserItem

class LabirintRuSpider(scrapy.Spider):
    name = 'labirint_ru'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/Python/?stype=0']

    def parse(self, response:HtmlResponse):
        next_page = response.css('a.pagination-next__text::attr(href)').extract_first()
        book_links = response.css('a.product-title-link::attr(href)').extract()

        print('labirint_ru', len(book_links))

        for link in book_links:
            yield response.follow(link, callback=self.book_parse)

        yield response.follow(next_page, callback=self.parse)

        pass


    def book_parse(self, response:HtmlResponse):
        id_p = response.url
        href_p = response.url
        name_p = response.css('div.prodtitle h1::text').extract_first()
        author_p = response.css('div.authors a::text').extract_first()
        price_new_p = response.css('span.buying-priceold-val-number::text').extract_first()
        price_old_p = response.css('span.buying-pricenew-val-number::text').extract_first()
        rate_p = response.css('#rate::text').extract_first()
        yield BookparserItem(_id=id_p, href=href_p, name=name_p, author=author_p, price_new=price_new_p, price_old=price_old_p, rate=rate_p)
