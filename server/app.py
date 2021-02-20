from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from main import evaluations, create_evaluations

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

filename = 'evaluations.csv'


@app.route("/")
def get_evaluations():
    create_evaluations(filename)
    return jsonify(evaluations(filename))
