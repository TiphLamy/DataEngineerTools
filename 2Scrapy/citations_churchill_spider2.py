import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        #réponse à la requête HTTP (l'attribut $text$ permet
        #d'accéder à son contenu)
        for cit in response.xpath('//li[@class="figsco__selection__list__evene__list__item"]'):
            text_container = cit.xpath('//div[@class="figsco__quote__text"]')
            author_container = cit.xpath('//div[@class="figsco__fake__col-9"]')
            
            text_value = text_container.xpath('a/text()').extract_first().translate({ord(i): None for i in 'u"\u201C"u"\u201D"'})
            author_name = author_container.xpath('a/text()').extract_first()
            
            yield { 'text' : text_value,
                    'author' : author_name }


