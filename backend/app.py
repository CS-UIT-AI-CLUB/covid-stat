from flask import Flask, request
from flask_pymongo import PyMongo
import time
import os

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://' + \
                            os.environ['MONGO_INITDB_ROOT_USERNAME'] + ':' + \
                            os.environ['MONGO_INITDB_ROOT_PASSWORD'] + '@' + \
                            'mongo:27017'
mongo = PyMongo(app)
db = mongo.covidstat

FETCH_INTERVAL = os.environ['FETCH_INTERVAL']

def query_timestamp():
    timestamp = request.args.get('timestamp', default = int(time.time()), type = int)
    t1 = timestamp - FETCH_INTERVAL//2
    t2 = timestamp + FETCH_INTERVAL//2
    return db.data.find({'timestamp', {'$gt': t1, '$lt': t2}})

@app.route("/provinces", methods=["GET"])
def get_provinces():
    return query_timestamp()['provinces']

@app.route("/vietnam", methods=["GET"])
def get_vietnam():
    return query_timestamp()['vietnam']

@app.route("/global", methods=["GET"])
def get_global():
    return query_timestamp()['global']