import scrapy

from Hockey_Team.items import HockeyTeamItem


class HockeyTeamSpider(scrapy.Spider):
    name = "hockey_team"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/?page_num=1"]

    def parse(self, response):
        teams = response.xpath('//table[@class="table"]/tr[@class="team"]')
        for each_team in teams:
            yield self.parse_each_team(each_team)

        next_page = response.xpath('//li/a[@aria-label="Next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_each_team(self, response):
        team_details = HockeyTeamItem()
        team_details["Team_Name"] = response.xpath('./td[@class="name"]/text()').get()
        team_details["Year"] = response.xpath('./td[@class="year"]/text()').get()
        team_details["Wins"] = response.xpath('./td[@class="wins"]/text()').get()
        team_details["Losses"] = response.xpath('./td[@class="losses"]/text()').get()
        team_details["OT_losses"] = response.xpath('./td[@class="ot-losses"]/text()').get()
        team_details["Goal_for"] = response.xpath('./td[@class="gf"]/text()').get()
        team_details["Goal_against"] = response.xpath('./td[@class="ga"]/text()').get()
        return team_details
