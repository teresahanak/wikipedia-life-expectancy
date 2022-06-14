
import scrapy


class ByYearSpider(scrapy.Spider):
    name = 'by_year'
    allowed_domains = ['en.wikipedia.org']
    # start_urls = ['https://en.wikipedia.org/wiki/Deaths_in_January_1994']

    def start_requests(self):
        yield scrapy.Request(url='https://en.wikipedia.org/wiki/Deaths_in_January_1994',
                             callback=self.parse,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                                       })
    def parse(self, response):
        container = response.xpath('//div[contains(@class, "mw-body-content")]/div')
        month_year = container.xpath('./h2/span/text()').get()
        days_of_month = response.xpath('//div[contains(@class, "hlist-separated")]/ul/li/a/text()').getall()
        days_of_month = [int(day) for day in days_of_month]

        for day in days_of_month:
            entries = container.xpath(f'./ul[{day+1}]/li')

            for entry in entries:
                day = day
                name = entry.xpath('./a[1]/text()').get()
                link = entry.xpath('./a[1]/@href').get()
                link = f'https://en.wikipedia.org{link}'

                info = ""
                for i, item in enumerate(entry.xpath('./text()').getall()):
                    info += item
                    if entry.xpath(f'./a[{i+2}]/text()'):
                        info += entry.xpath(f'./a[{i+2}]/text()').get()

                yield {
                    'month_year': month_year,
                    'day': day,
                    'name': name,
                    'info': info,
                    'link': link,
                    # 'User-Agent': response.request.headers['User-Agent'],
                }

        pagination = response.xpath('(//div[contains(@class, "hlist-separated")]/div/div/a)[2]')
        next_page_url = pagination.xpath('./@href').get()

        if next_page_url:
            yield response.follow(url=next_page_url,
                                  callback=self.parse,
                                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                                      })