import scrapy
from afl.items import AflItem

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
            item['round_1'] = row.xpath('td[14]//text()').extract_first()
            item['round_2'] = row.xpath('td[15]//text()').extract_first()
            item['round_3'] = row.xpath('td[16]//text()').extract_first()
            item['round_4'] = row.xpath('td[17]//text()').extract_first()
            item['round_5'] = row.xpath('td[18]//text()').extract_first()
            item['round_6'] = row.xpath('td[19]//text()').extract_first()
            item['round_7'] = row.xpath('td[20]//text()').extract_first()
            #item['round_8'] = row.xpath('td[21]//text()').extract_first()
            #item['round_9'] = row.xpath('td[22]//text()').extract_first()
            #player_id += 1
            yield item

# scrapy crawl dt -o dt.csv