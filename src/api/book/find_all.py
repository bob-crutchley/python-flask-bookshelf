from flask import Response
import pymysql.cursors
import json
import mysql

def execute():
    books = []
    connection = mysql.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Books;"
            cursor.execute(sql)
            books = cursor.fetchall()
            return Response(json.dumps(books), mimetype='application/json')
    finally:
        connection.close()
