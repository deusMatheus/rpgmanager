import sqlite3

class db_manager:

    def __init__(self):
        self.connection = sqlite3.connect('./data/database.db')
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, values_tuple):
        self.cursor.execute(f'CREATE TABLE {table_name} {values_tuple}')
        self.connection.commit()

    def insert_values(self, table_name, values_list):
        for value_string in values_list:
            self.cursor.execute(f"""INSERT INTO {table_name} VALUES {value_string}""")
        self.connection.commit()

    def delete_all(self):
        self.cursor.execute('DROP TABLE characters')
        self.cursor.execute('DROP TABLE players')
        self.cursor.execute('DROP TABLE dms')
        self.cursor.execute('DROP TABLE magic_items')
        self.cursor.execute('DROP TABLE users')
        self.cursor.execute('DROP TABLE posts')
        self.cursor.execute('DROP TABLE campaigns')
        self.cursor.execute('DROP TABLE log')
        self.connection.commit()

    def reset_all(self):
        self.delete_all()
        self.create_table('characters','(user_ID, name, class, archetype, origin, level, exp, gold)')
        self.create_table('players','(user_ID)')
        self.create_table('dms','(user_ID)')
        self.create_table('magic_items','(name, description, price)')
        self.create_table('users','(username, password, email, name, type)')
        self.create_table('posts','(user_ID, campaign_ID, subject, message, created_at)')
        self.create_table('campaigns','(title, description, game_link, dm_ID, players_IDs, posts_IDs, magic_items_IDs, current_status)')
        self.create_table('log','(date, time, table_name, user_id, operation_description)')

    def check_username(self, informedUsername, informedPassword):
#        print(self.cursor.execute(f'SELECT username, password FROM users WHERE username = "{informedUsername}" AND password = "{informedPassword}"').fetchall())
        return self.cursor.execute(f'SELECT username, password FROM users WHERE username = "{informedUsername}" AND password = "{informedPassword}"').fetchall()
    
    def get_user_name_by_username(self, informedUsername):
        return self.cursor.execute(f'SELECT name FROM users WHERE username = "{informedUsername}"').fetchall()[0][0]

#db_manager().reset_all()
#db_manager().insert_values('users',[f"('math_user','math_pass', 'math_email','math','dm')"])

#####
# CRIAR UM MÉTODO QUE PREENCHA TODAS AS TABELAS COM DADOS TESTE. AO REALIZAR O reset_all(), CHAMAR ESTE MÉTODO
####