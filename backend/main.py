from flask import Flask, jsonify
from flask_cors import CORS  # Добавьте эту строку
import sys
import os

# Импортируем функцию из post_parser.py
from post_parser import get_last_post


app = Flask(__name__)
CORS(app)

@app.route('/api/get_last_post')
def last_post():
    web_link = "https://web.telegram.org/k/#@akyur0"
    post_data = get_last_post(web_link)
    return jsonify(post_data)

if __name__ == '__main__':
    app.run(debug=True)