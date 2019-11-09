from flask import Blueprint

profile = Blueprint('books', __name__, url_prefix='/books')

import src.client.book.routes
import src.client.book.models
