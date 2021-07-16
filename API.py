import atexit
import time
import pickle
import secrets
import gzip
import os
import math
import random
from steamsignin import SteamSignIn

from flask import Flask, make_response, json, render_template, request, redirect, session, url_for
from flask_restful import Api, Resource, reqparse
from apscheduler.schedulers.background import BackgroundScheduler

def generate_secret():
    return secrets.token_urlsafe()

### SETUP THE API
app = Flask(__name__)
app.secret_key = generate_secret()
api = Api(app)
parser = reqparse.RequestParser()

### SETUP THE SCHEDULED JOBS
def random_job():
    print("Random job performed")
job_interval = 10 ## seconds
scheduler = BackgroundScheduler()
scheduler.add_job(func=random_job, trigger="interval", seconds=job_interval)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

### Make the classes for parsing and doing stuff with the actual requests

def returnError(errorStr):
    return {"status": False, "reason": errorStr}

def returnSuccess(data):
    return {"status": True, "data": data}

## TODO: Definitely improve the database LOL
class DataBase():
    verifiedUsers = []
    awaitingVerification = []

db = DataBase()
steam_base = 'https://steamcommunity.com/openid/login'
STEAMAPI = SteamSignIn()
redirect_url = "http://0.0.0.0:5000/verify/"


class ManageLogin(Resource):
    def get(self, hwid):
        db.awaitingVerification.append(hwid)
        login_url = STEAMAPI.ConstructURL(redirect_url + hwid)
        return returnSuccess({"task":"Login", "URL": f"{steam_base}?{login_url}"})

    def post(self):
        return returnError("Not allowed")

class VerifyLogin(Resource):

    def get(self, hwid):
        print(hwid)
        if hwid in db.awaitingVerification:
            steam_data = request.args
            print(steam_data)
            if STEAMAPI.ValidateResults(steam_data):
                ## LOL BULLSHIT DATABASE LOGIC:
                db.awaitingVerification.remove(hwid)
                db.verifiedUsers.append(hwid)
                return returnSuccess("Verification Successful")
            else:
                return returnError("Steam Verification Unsuccessful")
        else:
            ### Someone trying to do some bullshit. BLOCKK  the fucking IP
            return returnError("Not expecting verification by steam LOL.")


    def post(self, *args):
        return returnError("Not allowed")

### Register the endpoints

api.add_resource(ManageLogin, "/login/<string:hwid>")
api.add_resource(VerifyLogin, "/verify/<string:hwid>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")