# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/s?k=mobile&qid=1576588957&ref=sr_pg_1']
    page_number=2




    def parse(self, response):
        items = AmazonItem()


        product_name = response.css('.a-color-base.a-text-normal').extract()
        product_price = response.css('.a-price-whole').extract()
        product_image = response.css('.s-image').extract()


        items['product_name']=product_name
        items['product_brand']=product_brand
        items['product_price']=product_price
        items['product_image']=product_image


        yield items


        next_page='https://www.amazon.in/s?k=mobile&page='+str(AmazonSpiderSpider.page_number)+'&qid=1576588940&ref=sr_pg_2'

        if AmazonSpiderSpider.page_number<=100:
        	AmazonSpiderSpider.page_number+=1		
        	yield response.follow(next_page,callback=self.parse)





