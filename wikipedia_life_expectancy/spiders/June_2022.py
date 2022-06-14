import scrapy


class ReferencesSpider(scrapy.Spider):
    name = 'June_2022'
    allowed_domains = ['en.wikipedia.org']
    # start_urls = ['https://en.wikipedia.org/wiki/Deaths_in_2022#June']

    def start_requests(self):
        yield scrapy.Request(url='https://en.wikipedia.org/wiki/Deaths_in_2022#June',
                             callback=self.parse,
                             headers={
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                                 })

    def parse(self, response):
        day_containers = response.xpath('//div[contains(@class, "mw-body-content")]/div/ul')
        day_containers = day_containers[1:]
        day_containers = day_containers[:-2]

        for i, container in enumerate(day_containers):
            day = len(day_containers) - i
            entries = container.xpath(f'./li')

            for entry in entries:
                name = entry.xpath('./a[1]/text()').get()
                link = entry.xpath('./a[1]/@href').get()
                abs_url = response.urljoin(link)
                info = ""
                for i, item in enumerate(entry.xpath('./text()').getall()):
                    info += item
                    if entry.xpath(f'./a[{i+2}]/text()'):
                        info += entry.xpath(f'./a[{i+2}]/text()').get()

                yield scrapy.Request(url=abs_url,
                                     callback=self.parse_entry,
                                     meta={'day': day, 'name': name, 'link': abs_url, 'info': info},
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
        month_year = 'June 2022'
        day = response.request.meta['day']
        name = response.request.meta['name']
        info = response.request.meta['info']
        link = response.request.meta['link']
        references = response.xpath('//li[contains(@id, "cite_note")]').getall()
        num_references = len(references)

        yield {
            'month_year': month_year,
            'day': day,
            'name': name,
            'info': info,
            'link': link,
            'num_references': num_references
        }
