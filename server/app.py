from flask import Flask, jsonify
from main import evaluations, create_evaluations

app = Flask(__name__)

filename = 'evaluations.csv'


@app.route("/")
def get_evaluations():
    create_evaluations(filename)
    return jsonify(evaluations(filename))
