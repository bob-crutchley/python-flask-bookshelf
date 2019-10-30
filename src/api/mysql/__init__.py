import pymysql.cursors
import os

def get_connection():
    return pymysql.connect(host=(os.getenv("MYSQL_HOST") if os.getenv("MYSQL_HOST") else "localhost"),
                             user=(os.getenv("MYSQL_USER") if os.getenv("MYSQL_USER") else "root"),
                             password=(os.getenv("MYSQL_PASSWORD") if os.getenv("MYSQL_PASSWORD") else "password"),
                             db="bookshelf",
                             charset='utf8mb4')
