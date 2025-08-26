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

    def test_values(self):
        self.insert_values('users',[f"('akuma','akuma','akuma@akuma','akuma','player')"])
        self.insert_values('users',[f"('ken','ken','ken@ken','ken','player')"])
        self.insert_values('users',[f"('cammy','cammy','cammy@cammy','cammy','dm')"])
        self.insert_values('users',[f"('guile','guile','guile@guile','guile','player&dm')"])
        self.insert_values('players',[f"('{self.get_user_id_by_username('akuma')}')"])
        self.insert_values('players',[f"('{self.get_user_id_by_username('guile')}')"])
        self.insert_values('players',[f"('{self.get_user_id_by_username('ken')}')"])
        self.insert_values('dms',[f"('{self.get_user_id_by_username('guile')}')"])
        self.insert_values('dms',[f"('{self.get_user_id_by_username('cammy')}')"])
        self.insert_values('magic_items',[f"('Bead of Fireballs', 'Fireballs!!!!', '50000')"])
        self.insert_values('magic_items',[f"('Hand of Vecna', 'Eugh...', 'Not for sale')"])
        self.insert_values('characters',[f"('{self.get_user_id_by_username('akuma')}','Draco','Fighter','Arcane Archer','Dragonborn','1','0','300')"])
        self.insert_values('characters',[f"('{self.get_user_id_by_username('guile')}','Melf','Wizard','Evocation','Elf','5','6500','9000')"])
        self.insert_values('characters',[f"('{self.get_user_id_by_username('ken')}','John','Barbarian','Giant','Human','3','900','3000')"])
        self.insert_values('campaigns',[f"('Avernus', 'Hell all over the place', 'https://roll20.net/', '{self.get_user_id_by_username('cammy')}','({self.get_user_id_by_username('guile')},{self.get_user_id_by_username('akuma')})',('({self.get_character_id_by_name('Melf')},{self.get_character_id_by_name('Draco')})'),'0','{self.get_magicitem_id_by_name('Bead of Fireballs')}','active')"])
        self.insert_values('campaigns',[f"('Dragons', 'Dragons for fucks sake', 'https://roll20.net/', '{self.get_user_id_by_username('guile')}','({self.get_user_id_by_username('ken')},{self.get_user_id_by_username('akuma')})',('({self.get_character_id_by_name('John')},{self.get_character_id_by_name('Draco')})'),'0','{self.get_magicitem_id_by_name('Hand of Vecna')}','finished')"])

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
        self.create_table('campaigns','(title, description, game_link, dm_ID, players_IDs, characters_IDs, posts_IDs, magic_items_IDs, current_status)')
        self.create_table('log','(date, time, table_name, user_id, operation_description)')
        self.test_values()

    def check_username(self, informedUsername, informedPassword):
#        print(self.cursor.execute(f'SELECT username, password FROM users WHERE username = "{informedUsername}" AND password = "{informedPassword}"').fetchall())
        return self.cursor.execute(f'SELECT username, password FROM users WHERE username = "{informedUsername}" AND password = "{informedPassword}"').fetchall()
    
    def get_user_name_by_username(self, informedUsername):
        return self.cursor.execute(f'SELECT name FROM users WHERE username = "{informedUsername}"').fetchall()[0][0]
    
    def get_user_id_by_username(self, informedUsername):
        if(self.cursor.execute(f'SELECT rowid FROM users WHERE username = "{informedUsername}"').fetchall()):
            return self.cursor.execute(f'SELECT rowid FROM users WHERE username = "{informedUsername}"').fetchall()[0][0]
        return ''
    
    def get_magicitem_id_by_name(self, informedName):
        if(self.cursor.execute(f'SELECT rowid FROM magic_items WHERE name = "{informedName}"').fetchall()):
            return self.cursor.execute(f'SELECT rowid FROM magic_items WHERE name = "{informedName}"').fetchall()[0][0]
        return ''

    def get_character_id_by_name(self, informedName):
        if(self.cursor.execute(f'SELECT rowid FROM characters WHERE name = "{informedName}"').fetchall()):
            return self.cursor.execute(f'SELECT rowid FROM characters WHERE name = "{informedName}"').fetchall()[0][0]
        return ''

# db_manager().reset_all()
#db_manager().insert_values('users',[f"('math_user','math_pass', 'math_email','math','dm')"])

#####
# CRIAR UM MÉTODO QUE PREENCHA TODAS AS TABELAS COM DADOS TESTE. AO REALIZAR O reset_all(), CHAMAR ESTE MÉTODO
####
