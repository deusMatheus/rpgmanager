from classes.db_manager import db_manager as db

class Login_manager:

    def checkUser(self, informedUsername, informedPassword):
        if(db().check_username(informedUsername, informedPassword)):
            return True
        else:
            return False