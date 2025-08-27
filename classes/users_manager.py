from classes.db_manager import db_manager as db

class Users_manager:

    def get_user_name(self, informedUsername):
        return db().get_user_name_by_username(informedUsername)
    
    def get_type(self, informedUsername):
        return db().get_type_by_username(informedUsername)