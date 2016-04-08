# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem


class News163Spider(scrapy.Spider):
    name = "news163"
    allowed_domains = ["2kandy.com"]
    start_urls = (
        'http://2kandy.com/',
    )

    def parse(self, response):
	item = NewsItem()
	for url in response.xpath("//div[@class='c cl']/a"):
		v = url.xpath("@href").extract()
		print v	
		item['url'] = v
		yield item
		yield scrapy.Request(v[0],callback=self.parse_url)
	#find next page and continue ballback parse
	#for url in response.xpath("//span[@id='fd_page_top']/div/a[@class='nxt']/@href").extract():
	#	yield scrapy.Request(url,callback=self.parse)

    def parse_url(self,response):
	print response.xpath("//a[contains(@href,'baidu')][@target='_blank']/@href").extract()[1]
