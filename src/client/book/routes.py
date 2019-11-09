from flask import render_template
from src.client.book import profile

@profile.route("/all")
def get_all_books():
    books = [{"name": "test"}, {"name": "test2"}]
    return render_template('books/all.html', books=books)
