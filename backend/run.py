from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS, cross_origin
import requests
import os

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/random', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def random_number():
    data = {
        'randomNumber': randint(1, 100),
        'host': os.uname()[1]
    }
    response = jsonify(data)
    return response


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
