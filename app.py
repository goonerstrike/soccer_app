from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import requests
import json
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
#@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
	url = 'https://api.football-data.org/v1/competitions'
	headers = {'Authorization': 'Bearer 1310374de6494d8dbe31e7f84aa85f23'}
	r = requests.get(url, headers=headers, verify=False)
	competitions = r.json()
	leagues = []
	for i in competitions:
		leagues.append(i["caption"])
	return render_template('test.html', **locals())
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
