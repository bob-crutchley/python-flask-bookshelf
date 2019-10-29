 
from flask import Flask, request
from flask import Response

app = Flask(__name__, static_url_path='')

@app.route('/test')
def get_all_books():
	return "test"

if __name__ == "__main__":
    app.run()
