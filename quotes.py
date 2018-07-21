# -*- coding: utf-8 -*-

# the url i use: http://quotes.toscrape.com/random
#How to create a Scrapy spider using the selectors.
# Print the author name,tags and text
# save the file as a json file.
# You should know how to use google chrome inspector
# Know how to inspect the page elements
# Tutorial url: https://www.youtube.com/watch?v=qPvPiMbPSTE

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        # Using dictionary
        yield {
            'author_name':response.css('small.author::text').extract_first(),
            'text':response.css('span.text::text').extract_first(),
            'tags':response.css('a.tag::text').extract()
        }
