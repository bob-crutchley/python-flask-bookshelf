from flask import Flask, request, send_from_directory, Response, Blueprint

from book import profile as book_profile

app = Flask(__name__)
app.register_blueprint(book_profile)
