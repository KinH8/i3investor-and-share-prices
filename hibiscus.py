# -*- coding: utf-8 -*-
import scrapy
import re
from datetime import datetime, timezone, timedelta, time, date

def date_adjustor(x):
    if '-' in x:
        return x
    else:
        temp = x.split(' ')
        temp[0] = int(temp[0])
        if 'minute' in temp[1]:
            return datetime.today() + timedelta(minutes=-temp[0])
        elif 'hour' in temp[1]:
            return datetime.today() + timedelta(hours=-temp[0])
        elif 'day' in temp[1]:
            return datetime.today() + timedelta(days=-temp[0])
        elif 'week' in temp[1]:
            return datetime.today() + timedelta(weeks=-temp[0])
        elif 'month' in temp[1]:
            return datetime.today() + timedelta(days=-temp[0]*30)
        else:
            return datetime.today()

class HibSpider(scrapy.Spider):
    name = 'hib'
    allowed_domains = ['klse.i3investor.com/']
    start_urls = ['https://klse.i3investor.com/web/forum/forum-thread/800001960?p=1']
    custom_settings = {
            'FEED_URI' : 'tmp/hibiscus.csv',
            'FEED_FORMAT': "csv"
    }
       
    def parse(self, response):      
        rawdatetime = response.xpath('//span[@class="me-1"]/text()').extract()
        dates = [date_adjustor(z) for z in rawdatetime]
        
        number_of_posts = len(response.xpath('//span[@class="me-1"]/text()').extract())

        comments = []   
        for i in range(number_of_posts + 1):
            temp = response.xpath('//div[@class="card px-3 "]/div[{0}]//p[@class="comment"]//text()'.format(i)).extract()
            if i == 8:
                continue
            temp = ' '.join(w for w in temp)
            comments.append(temp)

        contributor = response.xpath('//a[@class="text-link"]/strong/text()').extract()
        postcount = response.xpath('//p[@class="subtitle"]/text()').re(r'\d+')
        
        for x in range(number_of_posts):
            yield {
                'Date': dates[x],
                'Name': contributor[x],
                'Comments': comments[x],
                'Postcount': postcount[x],
                }

        next_page = response.xpath('//ul[@class="pagination pagination-sm"]/li[-1]/a/@href').extract_first()
        main_site = 'https://klse.i3investor.com'

        if next_page:
            yield scrapy.Request(main_site + str(next_page),
                                 callback=self.parse, dont_filter = True)