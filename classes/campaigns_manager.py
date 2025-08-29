import streamlit as st
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
                if(len(Campaigns[i][4])>1):
                    players.append(db().get_user_name_by_id(Campaigns[i][4].split(",")[j]))
                else:
                    players.append(db().get_user_name_by_id(Campaigns[i][4]))

            for j in range(len(Campaigns[i][5].split(","))):
                if(len(Campaigns[i][5])>1):
                    characters.append(db().get_character_name_by_id(Campaigns[i][5].split(",")[j]))
                else:
                    characters.append(db().get_character_name_by_id(Campaigns[i][5]))

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
    
    def new_campaign(self, campaignTitle, campaignDescription):
        userId = db().get_user_id_by_username(st.session_state['username'])
        db().insert_values('campaigns',[f"('{campaignTitle}','{campaignDescription}','','{userId}','','','0','','On hold')"])
        userId = ''

    def add_player(self, player_to_add, campaign_title):
        db().add_player_to_campaign(player_to_add, campaign_title)

    def add_character(self, char_to_add, campaign_title):
        db().add_char_to_campaign(char_to_add, campaign_title)
