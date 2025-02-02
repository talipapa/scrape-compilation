import scrapy

class CatCampSpider(scrapy.Spider):
    name="catcampsitespider"
    allowed_domains=["wildkamp.ph"]
    
    start_urls=["https://wildkamp.ph/campsites"]

    def parse(self, response):
        provinces = response.css("ul.list-province")

        for province in provinces.css("li a::attr(href)"):
            yield response.follow(province.get(), self.parse_campsites)

    def parse_campsites(self, response):
        campsites = response.css("div.campsite-details")
        for campsite in campsites:
            yield {
                "name": campsite.css("h3 a::text").get(),
                "location": campsite.css("h4::text").get(),
                "link": campsite.css("h3 a::attr(href)").get()
            }
        


