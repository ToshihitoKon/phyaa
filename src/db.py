from pathlib import Path
import sqlite3
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry, sessionmaker

mapper_registry = registry()
class db:
    # singleton
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    dbname = 'sqlite:///phyaa.db'
    cursor = None
    connection = None
    def __init__(self):
        self.db = sqlalchemy.create_engine(self.dbname, echo=True)
        mapper_registry.metadata.create_all(bind=self.db)

    tags = []
    def write(self, tag):
        self.tags.append(tag)
    def read(self):
        return self.tags

@mapper_registry.mapped
class File:
    __tablename__ = 'file'
    id = Column(Integer)
    filename = Column(String(length=255),primary_key=True)

@mapper_registry.mapped
class Tag:
    __tablename__ = 'tag'
    id = Column(Integer)
    tagname = Column(String(length=255),primary_key=True)
    


# debug funcs
if __name__ == "__main__":
    print("ok")
    db1 = db()
    db2 = db()
    db1.write("by db1")
    db2.write("by db2")
    print(db1.read())
    print(db2.read())
