import pymysql.cursors
import os

def get_connection():
    return pymysql.connect(host=os.getenv("MYSQL_HOST"),
                             user=os.getenv("MYSQL_USER"),
                             password=os.getenv("MYSQL_PASSWORD"),
                             db=os.getenv("MYSQL_DATABASE"),
                             charset='utf8mb4')
