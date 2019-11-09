from flask import Flask, Blueprint, render_template, redirect, url_for
from src.client.book import profile as book_profile

app = Flask(__name__)
app.register_blueprint(book_profile)

@app.route('/', methods=['GET'])
def root():
    return redirect('/home')

@app.route('/home', methods=['GET'])
def home():
    content = "test"
    return render_template('index.html')

