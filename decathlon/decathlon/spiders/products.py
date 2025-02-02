import scrapy
import json

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["tq8i7i4sv5-dsn.algolia.net"]
    start_urls = ['https://tq8i7i4sv5-dsn.algolia.net/1/indexes/prod_pim_v2_index?hitsPerPage=20&facetFilters=[["categoryIds:a31b3a01-ed58-458e-97b1-0a330f9b0533"]]&page=' + str(x) for x in range(1, 50)]

    def parse(self, response):
        resp = json.loads(response.body)
        products = resp.get('hits')
        for product in products:
            # sports = product.get("sport_en")
            # for sport in sports:
            #     if sport in ["camping", "camping-tent", "Camping"]:
            yield {
                "name": product.get("name"),
                "brand": product.get("brand"),
                "price": product.get("price"),
                "stock_count": product.get("count"),
                "product_rating": product.get("rating"),
                "Availability": product.get("availability"),
                "url": "https://decathlon.ph" + product.get("url_en")
            }
        

        
