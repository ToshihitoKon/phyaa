#!/usr/bin/env python3
from pathlib import Path
import pymysql.cursors

music_suffixes = ['.mp3', '.aac', '.flac', '.m4a']

def search_entry(path):
    paths = []
    print(path)
    if path.is_dir():
        for child in path.iterdir():
            paths.extend(search_entry(child))
        return paths
    if path.is_file():
        if path.suffix in music_suffixes:
            return [path]
    return []

def mysql_sync_entry(paths):
    conn = pymysql.connect(host='db',
            user='root',
            db='phyaa_dev',
            charset='utf8mb4',
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor)

    strpaths = []
    for path in paths:
        strpaths.append([str(path)])

    query = 'INSERT INTO paths (hoge) VALUES (%s)'
    try:
        with conn.cursor() as cursor:
            print(cursor.executemany(query, strpaths))
            print(cursor.execute('select * from paths'))
            print(cursor.fetchall())
            #print(cursor.execute('drop table paths'))
    finally:
        conn.close()

if __name__ == '__main__':
    paths = search_entry(Path('.'))
    print(paths)
    #mysql_sync_entry(paths)
