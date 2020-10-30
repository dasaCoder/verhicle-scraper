import scrapy 
import json

class IkmanSpider(scrapy.Spider):
    name = "ikman"
    start_urls = [
        "https://ikman.lk/en/ads/sri-lanka/cars",
        "https://ikman.lk/en/ads/sri-lanka/vans-buses-lorries"
        ]

    def parse(self, response):
        for url in self.start_urls:
            for page_no in range(5):
                final_url = url + "?page=" + str(page_no)
                yield scrapy.Request(final_url, dont_filter=True, callback=self.scrapeList)

    def scrapeList(self, response):
        base_url = "https://ikman.lk"

        link_list = response.xpath("//*[contains(@class, 'normal--2QYVk gtm-normal-ad')]//a/@href")

        for link in link_list:
            yield scrapy.Request(base_url + link.get(), dont_filter=True, callback=self.scrapeSinglePage)

    def scrapeSinglePage(self, response):

        addvertiesment = response.xpath(".//div[contains(@class, 'section--PpGYD')]")
        details = addvertiesment.xpath(".//*[contains(@class, 'two-columns--19Hyo')]")

        record = {}
        for infor in details:
            key = infor.xpath(".//*[contains(@class, 'word-break--2nyVq label--3oVZK')]//text()").extract_first()
            value = infor.xpath(".//*[contains(@class, 'word-break--2nyVq value--1lKHt')]//text()").extract_first()

            record[key] = value
        

        return record


            