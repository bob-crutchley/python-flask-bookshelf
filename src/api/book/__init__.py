from flask import Blueprint
from . import find_all

profile = Blueprint('book', __name__, url_prefix='/book')

@profile.route("/find-all")
def get_all_books():
    return find_all.execute()
