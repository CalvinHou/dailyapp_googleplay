#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sqlite3
con = sqlite3.connect(":memory:")

# 创建表
con.execute("""
        CREATE TABLE todo
        (
            id INTEGER PRIMARY KEY,
                title TEXT,
                pkg TEXT
                );""")

# 创建表：效果相同
'''
con.execute("""
CREATE TABLE todo
(
    id INTEGER PRIMARY KEY NOT NULL,
        title TEXT
        );""")
'''

# 插入记录：shopping
#con.execute("INSERT INTO todo (title) VALUES ('shopping');")
test = "myname"
pkg = "com.test"
con.execute("INSERT INTO todo (title, pkg) VALUES (?, ?);", (test, "com.test"))

# 插入记录：working
con.execute("INSERT INTO todo (id, title, pkg) VALUES (NULL, 'working', 'com.test');")

# 查询记录
for row in con.execute("SELECT * FROM todo"):
    print row
