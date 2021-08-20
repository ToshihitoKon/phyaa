from pathlib import Path
import sqlite3

class db:
    __instance
    def __init__(self):
        if __instance == None:
        self.connection = sqlite3.connect('phyaa.db')
        self.cur = connection.cursor()

    def read(self, key):


# singletone
def get_db():
    if db == None:
        db = db()
    return db
