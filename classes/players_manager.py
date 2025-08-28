import streamlit as st
from classes.db_manager import db_manager as db

class Players_manager:

    def get_characters(self, informedUsername):
        informedId = db().get_user_id_by_username(informedUsername)
        listOfCharacters = []
        if(len(db().get_characters_by_userid(informedId))>1):
            for i in range(len(db().get_characters_by_userid(informedId))):
                characterDict = {
                    'name': db().get_characters_by_userid(informedId)[i][1],
                    'class': db().get_characters_by_userid(informedId)[i][2],
                    'archetype': db().get_characters_by_userid(informedId)[i][3],
                    'origin': db().get_characters_by_userid(informedId)[i][4],
                    'level': db().get_characters_by_userid(informedId)[i][5],
                    'exp': db().get_characters_by_userid(informedId)[i][6],
                    'gold': db().get_characters_by_userid(informedId)[i][7],
                }
                listOfCharacters.append(characterDict)
        elif(len(db().get_characters_by_userid(informedId))==1):
            characterDict = {
                'name': db().get_characters_by_userid(informedId)[0][1],
                'class': db().get_characters_by_userid(informedId)[0][2],
                'archetype': db().get_characters_by_userid(informedId)[0][3],
                'origin': db().get_characters_by_userid(informedId)[0][4],
                'level': db().get_characters_by_userid(informedId)[0][5],
                'exp': db().get_characters_by_userid(informedId)[0][6],
                'gold': db().get_characters_by_userid(informedId)[0][7],
            }
            listOfCharacters.append(characterDict)
        return listOfCharacters
    
    def new_character(self, charName, charOrigin, charClass, charArchetype, charLevel, charExp, charGold):
        userId = db().get_user_id_by_username(st.session_state['username'])
        db().insert_values('characters',[f"('{userId}','{charName}','{charClass}','{charArchetype}','{charOrigin}','{charLevel}','{charExp}','{charGold}')"])
#        self.insert_values('characters',[f"('{self.get_user_id_by_username('akuma')}','Draco','Fighter','Arcane Archer','Dragonborn','1','0','300')"])
        userId = ''