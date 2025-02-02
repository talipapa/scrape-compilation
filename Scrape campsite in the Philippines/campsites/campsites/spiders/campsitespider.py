import scrapy
import re

class CampsitespiderSpider(scrapy.Spider):
    name = "campsitespider"
    allowed_domains = ["campsites.ph"]

    start_urls = ['https://campsites.ph/explore?category=1&sort=2&show=3&page='+str(x) for x in range(1, 10)]

    def parse(self, response):
        campsites = response.css("div.card")

        for campsite in campsites:
            price = campsite.css("div.h-100 div.gap-3 a.fs-15 span::text").get(default="")
            cleanPrice = re.sub(r'[^\d]', '', price)

            yield{
                'link': campsite.css("a.stretched-link ::attr(href)").get(),
                'name': campsite.css("h4::text").get(default="").strip() or  "Name not found",
                'price': cleanPrice,
                'location': campsite.css("div.h-100 a.fs-13 span.text-capitalize::text").get()
            }
