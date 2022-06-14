import scrapy
import pandas as pd


class Refs3Spider(scrapy.Spider):
    name = 'refs5'
    allowed_domains = ['en.wikipedia.org']

    # start_urls = ['http://en.wikipedia.org/']

    def start_requests(self):
        rescrape_df = pd.read_csv('rescrape_df_4th.csv')
        rescrape_lst = rescrape_df['link'].to_list()
        for link in rescrape_lst:
            yield scrapy.Request(url=link,
                                 callback=self.parse,
                                 headers={
                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'},
                                 meta={'link': link},
                                 )

    def parse(self, response):
        references = response.xpath('//ol[@class="references"]/li').getall()
        num_references = len(references)

        yield {
            'link': response.request.meta['link'],
            'num_references': num_references,
        }
