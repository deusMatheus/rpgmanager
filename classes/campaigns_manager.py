import pprint as pp
from classes.db_manager import db_manager as db

class Campaigns_manager:

    def list_campaigns(self):
        Campaigns = db().list_campaigns()
        organizedCampaigns = []
        for i in range(len(Campaigns)):
            players = []
            characters = []
#            magicItems = []
            
            for j in range(len(Campaigns[i][4].split(","))):
                players.append(db().get_user_name_by_id(Campaigns[i][4].split(",")[j]))
                characters.append(db().get_character_name_by_id(Campaigns[i][5].split(",")[j]))

#            for j in range(len(Campaigns[i][7].split(","))):
#                magicItems.append(db().get_magicitem_name_by_id(Campaigns[i][7].split(","))[j])

            campaignsDict = {
                'title': Campaigns[i][0],
                'description': Campaigns[i][1],
                'url': Campaigns[i][2],
                'dm' : db().get_user_name_by_id(Campaigns[i][3]),
                'players': players,
                'characters': characters,
                'posts': Campaigns[i][6],
                'magic_items': db().get_magicitem_name_by_id(Campaigns[i][7]),
                'status': Campaigns[i][8]
            }
            organizedCampaigns.append(campaignsDict)
        return organizedCampaigns
    