from flask import Flask, request
from flask_pymongo import PyMongo
import time
import os

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://' + \
                            os.environ['MONGO_INITDB_ROOT_USERNAME'] + ':' + \
                            os.environ['MONGO_INITDB_ROOT_PASSWORD'] + '@' + \
                            'mongo:27017/covidstat?authSource=admin'
mongo = PyMongo(app)
db = mongo.db

FETCH_INTERVAL = int(os.environ['FETCH_INTERVAL'])

def query_timestamp():
    timestamp = request.args.get('timestamp', default = int(time.time()), type = int)
    t1 = timestamp - FETCH_INTERVAL
    t2 = timestamp + FETCH_INTERVAL
    return db.data.find_one({'timestamp': {'$gt': t1, '$lt': t2}})

@app.route("/provinces", methods=["GET"])
def get_provinces():
    res = query_timestamp()
    if res:
        return res['provinces']
    else:
        return {}, 404

@app.route("/vietnam", methods=["GET"])
def get_vietnam():
    res = query_timestamp()
    if res:
        return res['vietnam']
    else:
        return {}, 404

@app.route("/global", methods=["GET"])
def get_global():
    res = query_timestamp()
    if res:
        return res['global']
    else:
        return {}, 404