import scrapy


class NationsSpider(scrapy.Spider):
    name = 'nations'
    allowed_domains = ['www.worldatlas.com']
    start_urls = ['https://www.worldatlas.com/articles/what-is-a-demonym-a-list-of-nationalities.html']

    def parse(self, response):
        countries = response.xpath('//tbody')
        # countries = body.xpath('./tr')

        for country in countries:
            country = countries.xpath('./tr/td[1]/text()').get()
            nationality = countries.xpath('.tr/td[2]/text()').get()

            yield {
                'country': country,
                'nationality': nationality
            }


