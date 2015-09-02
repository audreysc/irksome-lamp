import os
from bottle import run, template, get, post, request

import plotly.plotly as py
from plotly.graph_objs import *

import data as d
import places as p
from collections import OrderedDict
import json

# grab username and key from config/data file
with open('data.json') as config_file:
    config_data = json.load(config_file)
username = config_data["user"]
key = config_data["key"]

py.sign_in(username, key)
# add your username and api key

@get('/plot')
def form():
    return template('templateform', title='Plot.ly Graph')


@post('/plot')
def submit():
    # grab data from form
    ID = request.forms.get('ID')
    NAME = request.forms.get('NAME')
    all_runners = d.start_graph_race(ID)
    plot_url = p.graph_ranks_runner(all_runners, NAME)
    return template('embedgraph', title='Plot.ly Graph', plot_url=str(plot_url))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
