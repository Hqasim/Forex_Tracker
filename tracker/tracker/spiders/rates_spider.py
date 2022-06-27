import scrapy

class RatesSpider(scrapy.Spider):
    name = "rates"

    # URL to scrape data from
    start_urls = [
        "https://www.forex.pk/foreign-exchange-rate.html"
    ]

    # Parses the URL and extracts data
    def parse(self, response):
        # Extract table data (Units per USD)
        update_time = response.xpath("/html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/span/text()").get()
        CNY = response.xpath("//html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[3]/td[3]/text()").get()
        EUR = response.xpath("//html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[4]/td[3]/text()").get()
        JPY = response.xpath("//html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[5]/td[3]/text()").get()
        PKR = response.xpath("//html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[6]/td[3]/text()").get()
        SAR = response.xpath("//html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[7]/td[3]/text()").get()
        AED = response.xpath("//html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[8]/td[3]/text()").get()
        GBP = response.xpath("//html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[9]/td[3]/text()").get()
        
        yield {
            "Title": "Forex Curreny Rates " + update_time,
            "CNY": CNY + " Units per USD",
            "EUR": EUR + " Units per USD",
            "JPY": JPY + " Units per USD",
            "PKR": PKR + " Units per USD",
            "SAR": SAR + " Units per USD",
            "AED": AED + " Units per USD",
            "GBP": GBP + " Units per USD",
        }




#  /html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[6]/td[3]
# //html/body/table/tr[1]/td[2]/table/tr[3]/td/table/tr[1]/td/table/tr/td[2]/table/tr[6]/td[3]/text()