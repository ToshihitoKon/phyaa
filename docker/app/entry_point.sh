#!/usr/bin/env sh

python3 -m pip install pymysql[rsa]

# dbが立ち上がるまで雑に待つ
sleep 20
python3 /usr/src/app/src/main.py
