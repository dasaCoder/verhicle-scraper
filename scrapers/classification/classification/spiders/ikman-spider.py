import scrapy 
import json

class IkmanSpider(scrapy.Spider):
    name = "ikman"
    start_urls = ["https://ikman.lk/en/ad/mercedes-benz-c200-kompressor-2007-for-sale-colombo-1"]

    def parse(self, response):

        addvertiesment = response.xpath(".//div[contains(@class, 'section--PpGYD')]")
        details = addvertiesment.xpath(".//*[contains(@class, 'two-columns--19Hyo')]")

        record = {}
        for infor in details:
            key = infor.xpath(".//*[contains(@class, 'word-break--2nyVq label--3oVZK')]//text()").extract_first()
            value = infor.xpath(".//*[contains(@class, 'word-break--2nyVq value--1lKHt')]//text()").extract_first()

            record[key] = value
        

        return record


            