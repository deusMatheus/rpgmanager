from classes.db_manager import db_manager as db
from classes.email_manager import Email

class Users_manager:

    def get_user_name(self, informedUsername):
        return db().get_user_name_by_username(informedUsername)
    
    def get_type(self, informedUsername):
        return db().get_type_by_username(informedUsername)
    
    def check_username_availability(self, informedUsername):
        listFromDB = db().list_usernames()
        listOfUsernames = []
        for username in listFromDB:
            listOfUsernames.append(username[0])
#        print(listOfUsernames)
        if(informedUsername in listOfUsernames):
            return True
        return False
    
    def register_new_user(self, informedName, informedUsername, informedEmail):
        otp = Email().generate_one_time_password()
        subject = 'Cadastro de novo usuário em RPG Manager'
        body = f'''
            Olá {informedName}!
            
            Seja bem-vindo ao RPG Manager!
            
            Seu código para cadastro é {otp}.
            
            Caso não tenha registrado, favor ignorar este e-mail.

            Atenciosamente,
            Equipe RPG Manager.
            '''
        Email().send_email(informedEmail,subject, body)
        db().insert_values('temp', [f"('{informedUsername}',{otp}, 'active')"])

    def check_otp(self, informedName, informedUsername, informedPass, informedEmail, informedOTP):
        if(db().check_otp(informedUsername, informedOTP)):
            db().register_new_user(informedUsername, informedPass, informedEmail, informedName)
            return True
        return False