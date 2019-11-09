from flask import render_template
from src.client.book import profile

@profile.route("/all")
def get_all_books():
    return render_template('books/all.html')
