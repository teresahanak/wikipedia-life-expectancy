import scrapy


class ReferencesSpider(scrapy.Spider):
    name = 'references'
    allowed_domains = ['en.wikipedia.org']

    # start_urls = ['https://en.wikipedia.org/wiki/Deaths_in_January_1994']

    def start_requests(self):
        yield scrapy.Request(url='https://en.wikipedia.org/wiki/Deaths_in_January_1994',
                             callback=self.parse,
                             headers={
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                                 })

    def parse(self, response):
        container = response.xpath('//div[contains(@class, "mw-body-content")]/div')
        days_of_month = response.xpath('//div[contains(@class, "hlist-separated")]/ul/li/a/text()').getall()
        days_of_month = [int(day) for day in days_of_month]

        for day in days_of_month:
            entries = container.xpath(f'./ul[{day + 1}]/li')

            for entry in entries:
                link = entry.xpath('./a[1]/@href').get()
                abs_url = response.urljoin(link)
                yield scrapy.Request(url=abs_url,
                                     callback=self.parse_entry,
                                     meta={'link': abs_url},
                                     headers={
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                                     }
                                     )

        pagination = response.xpath('(//div[contains(@class, "hlist-separated")]/div/div/a)[2]')
        next_page_url = pagination.xpath('./@href').get()

        if next_page_url:
            yield response.follow(url=next_page_url,
                                  callback=self.parse,
                                  headers={
                                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                                  })

    def parse_entry(self, response):
        link = response.request.meta['link']
        references = response.xpath('//li[contains(@id, "cite_note")]').getall()
        num_references = len(references)

        yield {
            'link': link,
            'num_references': num_references
        }
