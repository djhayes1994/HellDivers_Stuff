# https://helldiverstrainingmanual.com/api
import rest_client

hd = rest_client.client()

class helldivers:
    def __init__(self) -> None:
        pass
    
    #News actually doesn't do anything because I'm not quite sure what to grab from it and the war/campaign endpoint seems to have more useful info might add later who knows.
    def news(self):
        news = hd.request(endpoint="war/news")
        return news
    
    def campaigns(self, major_order=False):
        campaigns = hd.request(endpoint='war/campaign')
        if "ERROR:" not in campaigns:
            if major_order == True:
                major_list = []
                for campaign in campaigns:
                    if campaign['majorOrder'] == True:
                        major_list.append(campaign)
                return major_list
            else:
                return campaigns
        else:
            return campaigns
        