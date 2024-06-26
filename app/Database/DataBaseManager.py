import sqlite3

db_name = 'Database.sqlite'


class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_database(self):
        """ Создание базы данных, если она не существует """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_users_table(self):
        create_table_query = '''
         CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255),
                first_name_tg VARCHAR(255),
                last_name_tg VARCHAR(255),
                username_tg VARCHAR(255),
                user_position VARCHAR(255) DEFAULT 'Пользователь',
                count_orders VARCHAR(255),
                city VARCHAR(255),
                address VARCHAR(255),
                firstname VARCHAR(255),
                surname VARCHAR(255),
                lastname VARCHAR(255),
                phone_number VARCHAR(255),
                active_delivery BOOLEAN,
                pers_loyalty VARCHAR(255),
                pers_referal_link VARCHAR(255),
                from_referal_link VARCHAR(255)
            )
       '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def create_manager_table(self):
        create_table_query = '''
         CREATE TABLE IF NOT EXISTS manager (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255),   
                firstname VARCHAR(255),
                lastname VARCHAR(255),
                username VARCHAR(255),
                ticket_count INTEGER,
                open_ticket_count INTEGER
            )
       '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def get_info_for_manager(self, user_id):
        query = "SELECT * FROM manager WHERE user_id = ?"
        self.cursor.execute(query, (user_id,))
        manager_info = self.cursor.fetchone()
        return manager_info

    def create_admin_table(self):
        create_table_query = '''
         CREATE TABLE IF NOT EXISTS admin_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255),   
                firstname VARCHAR(255),
                lastname VARCHAR(255),
                username VARCHAR(255),
                count_users INTEGER,
                count_pers INTEGER
            )
       '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def get_info_for_admin(self, user_id):
        query = "SELECT * FROM admin_table WHERE user_id = ?"
        self.cursor.execute(query, (user_id,))
        admin_info = self.cursor.fetchone()
        return admin_info

    def insert_into_users_table(self, user_data):
        """ Проверяем, существует ли запись с данным user_id """
        user_id = user_data['user_id']
        self.cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        existing_user = self.cursor.fetchone()

        if not existing_user:
            """ Если записи с таким user_id нет, то вставляем новую запись """
            insert_query = '''
                INSERT INTO users (user_id, first_name_tg, last_name_tg, username_tg, user_position, count_orders, 
                                   city, address, firstname, surname, lastname, phone_number, active_delivery, 
                                   pers_loyalty, pers_referal_link, from_referal_link) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            values = tuple(user_data.values())
            self.cursor.execute(insert_query, values)
            self.conn.commit()

    def get_actual_info_for_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = ?"
        self.cursor.execute(query, (user_id,))
        user_info = self.cursor.fetchone()
        return user_info

    def get_user_position(self, user_id):
        query = "SELECT user_position FROM users WHERE user_id = ?"
        self.cursor.execute(query, (user_id,))
        user_position = self.cursor.fetchone()
        for position in user_position:
            return position

    def get_fullname(self, user_id):
        query = "SELECT firstname, surname, lastname FROM users WHERE user_id = ?"
        self.cursor.execute(query, (user_id,))
        fullname = self.cursor.fetchone()
        return fullname


