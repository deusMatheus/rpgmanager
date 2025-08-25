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
        self.create_table('characters','(name, class, origin, level, exp, gold)')
        self.create_table('players','(user_ID, character_IDs, campaign_IDs)')
        self.create_table('dms','(user_ID, campaign_IDs)')
        self.create_table('magic_items','(name, description, price)')
        self.create_table('users','(username, password, name, type, posts_IDs)')
        self.create_table('posts','(user_ID, campaign_ID, subject, message, created_at)')
        self.create_table('campaigns','(title, description, game_link, dm_ID, players_IDs, posts_IDs, magic_items_IDs)')
        self.create_table('log','(date, time, table_name, user_id, operation_description)')

db_manager().reset_all()