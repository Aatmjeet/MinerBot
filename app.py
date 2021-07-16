import requests
from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime, timedelta
import time
import json
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))
from steamsignin import SteamSignIn
import waitress

app = Flask(__name__)

@app.route('/')
def main():
    shouldLogin = request.args.get('login')
    if shouldLogin is not None:
        steamLogin = SteamSignIn()
        # Flask expects an explicit return on the route.
        return steamLogin.RedirectUser(steamLogin.ConstructURL('http://localhost:8080/processlogin'))

    return 'Click <a href="/?login=true">to log in</a>'

@app.route('/processlogin')
def process():
    returnData = request.values
    steamLogin = SteamSignIn()
    steamID = steamLogin.ValidateResults(returnData)
    print('SteamID returned is: ', steamID)
    if steamID is not False:
        return 'We logged in successfully!<br />SteamID: {0}'.format(steamID)
    else:
        return 'Failed to log in, bad details?'

	# Sun, yahan se redierect kar skte hai.

if __name__ == "__main__":
    #app.debug = False
    #port = int(os.environ.get('PORT', 33507))
    #waitress.serve(app, port = port)
    app.run(host = 'localhost', port = 8080, debug = False)
