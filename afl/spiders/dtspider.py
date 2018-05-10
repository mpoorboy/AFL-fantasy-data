import scrapy
from afl.items import AflItem
#from scrapy.spiders import CrawlSpider
#from scrapy import Selector
#from scrapy.item import Item, Field

class dtspider(scrapy.Spider):
    name = "dt"
    allowed_domains = ["dtlive.com.au"]
    start_urls = ["http://dtlive.com.au/afl/dataview.php"]

    def parse(self, response):
        rows = response.xpath('//table[@class="tablesorter"]//tr')
        #player_id = 1
        for row in rows:
            item = AflItem()
            #item['player_id'] = [player_id]
            item['player'] = row.xpath('td[2]//text()').extract_first()
            item['position'] = row.xpath('td[3]/text()').extract_first()
            item['start_price'] = row.xpath('td[4]/text()').extract_first()
            item['current_price'] = row.xpath('td[6]/text()').extract_first()
            item['own'] = row.xpath('td[7]/text()').extract_first()
            item['games'] = row.xpath('td[8]/text()').extract_first()
            item['be'] = row.xpath('td[13]/text()').extract_first()
            #player_id += 1
            yield item

# scrapy crawl dt -o dt.csv