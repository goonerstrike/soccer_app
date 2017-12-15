from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import requests
import json

app = Flask(__name__)

comp_url = 'https://api.football-data.org/v1/competitions'
headers = {'Authorization': 'Bearer 1310374de6494d8dbe31e7f84aa85f23'}

@app.route("/")
def index():
  r = requests.get(comp_url, headers=headers, verify=False)
  competitions = r.json()
  league_name = []
  league_acronym = []
  for i in competitions:
      league_name.append(i["caption"])
  for a in competitions:
      league_acronym.append(a["league"])
  leagues = zip(league_acronym, league_name)
  return render_template('index.html', **locals())


@app.route("/PL/")
def epl():
  url = 'https://api.football-data.org/v1/competitions/445/teams'
  r = requests.get(url, headers=headers, verify=False)
  squads = r.json()
  team_name = []
  team_logo = []
  for i in squads["teams"]:
      team_name.append(i["shortName"])
      team_logo.append(i["crestUrl"])
      teams = zip(team_name, team_logo)
  return render_template('/PL/index.html', **locals())


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
