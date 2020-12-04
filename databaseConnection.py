import sqlite3
from sqlite3 import Error
from emojiUsage import EmojiUsage
import time


class Database:
    connected = False
    connection = None

    def __init__(self, path):
        try:
            self.connection = sqlite3.connect(path)
            self.connected = True
            self.c = self.connection.cursor()
            self.create_database()
        except Error as e:
            print(f"The error '{e}' occurred")

    def add_data(self, author, channel, time, emoji, server):
        # Insert a row of data
        t = (author,channel,time,emoji,server)
        self.c.execute('INSERT INTO emojiUses (author_id,channel,time,emoji,server) VALUES (?,?,?,?,?)',t)
        self.connection.commit()

    def load_data(self):
        counterList = []

        for row in self.c.execute('SELECT * FROM emojiUses'):
            counterList.append(EmojiUsage(row[0],row[1],row[2],row[3],row[4],row[5]))

        return counterList

    def create_database(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS emojiUses
             (usage_id INTEGER PRIMARY KEY, author_id int, channel int, time text, emoji text, server text)''')
        self.connection.commit()


# data.create_database()
#
# data.add_data(19292,'general','13:10',':joe:','Spooky Show')





