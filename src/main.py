#!/usr/bin/env python3
from pathlib import Path
import pymysql.cursors

music_suffixes = ['.mp3', '.aac', '.flac', '.m4a']

def search_entry(path):
    paths = []
    if path.is_dir():
        for child in path.iterdir():
            paths.extend(search_entry(child))
        return paths
    if path.is_file():
        if path.suffix in music_suffixes:
            return [path]
    return []

def mysql_sync_entry(paths):
    conn = pymysql.connect(
            host='db',
            user='root',
            password='password',
            db='phyaa_dev',
            charset='utf8mb4',
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor)

    strpaths = []
    for path in paths:
        strpaths.append([str(path)])

    query = 'INSERT INTO files (filepath) VALUES (%s)'
    try:
        with conn.cursor() as cursor:
            print(cursor.executemany(query, strpaths))
            print(cursor.execute('select * from files'))
            print(cursor.fetchall())
            #print(cursor.execute('drop table paths'))
    finally:
        conn.close()

if __name__ == '__main__':
    paths = search_entry(Path('.'))
    mysql_sync_entry(paths)
