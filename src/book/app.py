from flask import Flask, request, send_from_directory
from flask import Response
import pymysql.cursors
import os
import json

app = Flask(__name__, static_url_path='')

def get_connection():
    return pymysql.connect(host="localhost",
                             user="root",
                             password="password",
                             db=os.getenv("MYSQL_DATABASE"),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/api/books/all')
def get_all_books():
    books = []
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Books;"
            cursor.execute(sql)
            books = cursor.fetchall()
            return Response(json.dumps(books), mimetype='application/json')
    finally:
        connection.close()

@app.route('/api/books/all')
def get_all_books():
    books = []
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO Books (Name,Author,Image) VALUES ("' + name + '","' + author + '","' + image + '");'
            cursor.execute(sql)
            response = {
                message: "OK" 
            }
            return Response(json.dumps(response), mimetype='application/json')
    finally:
        connection.close()
