import scrapy
from scrapy import Request
#from items import ArticleItem
class LemondeSpider(scrapy.Spider):
    name = "billboard"
    #allowed_domains = ['lemonde.fr']
    #start_urls = ['http://lemonde.fr/']
    allowed_domains = ["www.billboard.com/charts/billboard-200"]
    start_urls = ['https://www.billboard.com/charts/billboard-200']

    def parse(self, response):
        #title = response.css('title::text').extract_first()
        album = response.css("span.chart-element__information")[1].css("span.chart-element__information__song.text--truncate.color--primary::text").extract_first()#__information__song.text--truncate.color--primary::text")[3].extract_first()
        artist = response.css("span.chart-element__information")[1].css("span.chart-element__information__artist.text--truncate.color--secondary::text").extract_first()
	#chart-liste = response.css('span::text').extract_first()
        #chart-liste = response.css("span::chart-element__information__song.text--truncate.color--primary").get()
        #title = response.css('title::text').extract_first()
        #all_links = {
         #   name:response.urljoin(url) for name, url in zip(
          #  response.css("#nav-markup .Nav__item")[3].css("a::text").extract(),
           # response.css("#nav-markup .Nav__item")[3].css("a::attr(href)").extract())
        #}
        yield {
            "album":album,
            "artist":artist
            #"chart-liste":chart-liste
            #"all_links":all_links
        }     
	
	#all_links = {
            #name:response.urljoin(url) for name, url in zip(
            #response.css("#nav-markup .Nav__item")[3].css("a::text").extract(),
            #response.css("#nav-markup .Nav__item")[3].css("a::attr(href)").extract())
        #}
        #for link in all_links.values():
         #   yield Request(link, callback=self.parse_category)

   # def parse_category(self, response):
        #for article in response.css(".river")[0].css(".teaser"):
         #   title = self.clean_spaces(article.css("h3 ::text").extract_first())
          #  image = article.css("img::attr(data-src)").extract_first()
           # description = article.css("p::text").extract_first()

           # yield ArticleItem(
            #    title=title,
             #   image=image,
              #  description=description
            #)

    def clean_spaces(self, string):
        if string is not None:
            return " ".join(string.split())
