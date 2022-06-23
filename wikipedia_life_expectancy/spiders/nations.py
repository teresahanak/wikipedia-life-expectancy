import scrapy


class NationsSpider(scrapy.Spider):
    name = 'nations'
    allowed_domains = ['www.worldatlas.com']
    start_urls = ['https://www.worldatlas.com/articles/what-is-a-demonym-a-list-of-nationalities.html']

    def parse(self, response):
        countries = response.xpath('//tbody/tr')

        for country in countries:
            country_name = country.xpath('./td[1]/text()').get()
            nationality = country.xpath('./td[2]/text()').get()

            yield {
                'country': country_name,
                'nationality': nationality
            }


