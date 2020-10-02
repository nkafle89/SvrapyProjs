import scrapy


class BusCompanyScraperSpider(scrapy.Spider):
    name = 'BusCompanyScraper'
    start_urls = ['https://www.turkiyeotobusfirmalari.com/otobus-bileti/otobus-firmalari.html']

    def parse(self, response):

        all_companies = response.css(".col-xs-6.col-sm-3").css("p")

        for company in all_companies:
            name = company.css("a::attr(title)").extract_first()
            link = company.css("a::attr(href)").extract_first()
            '''
            if link:
                yield scrapy.Request(response.urljoin(link), callback=self.parse2)
            '''
            scarped_info = {
                'name': name,
                'website': link,
            }
            yield scarped_info


    def parse2(self, response):
        pass
