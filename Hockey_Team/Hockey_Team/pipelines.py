# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class HockeyTeamPipeline:
    def process_item(self, item, spider):
        hockey_cleaning_data = ItemAdapter(item)

        field_names = hockey_cleaning_data.field_names()
        for i in field_names:
            hockey_cleaning_data[i] = hockey_cleaning_data.get(i).strip()

        if hockey_cleaning_data["OT_losses"] == "":
            raise DropItem("OT Lossess DATA is not there in web")

        for i in field_names:
            if i != "Team_Name":
                hockey_cleaning_data[i] = int(hockey_cleaning_data[i])

        return item
