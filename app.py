import os
from bottle import run, template, get, post, request

import plotly.plotly as py
from plotly.graph_objs import *

import data as d
import places as p
from collections import OrderedDict
import json

# For development
# grab username and key from config/data file
#with open('data.json') as config_file:
#    config_data = json.load(config_file)
#username = config_data["user"]
#key = config_data["key"]
#racery_base_url = config_data["url"]

# For production
username = os.environ["PLOTLY_USER"]
key = os.environ["PLOTLY_KEY"]

# Plotly signin
py.sign_in(username, key)


@get('/')
def wrong():
    redirect("/plot")

@get('/plot')
def form():
    return template('templateform', title='Plot.ly Graph')


@post('/plot')
def submit():
    # grab data from form
    ID = request.forms.get('ID')
    NAME = request.forms.get('NAME')
    urls = d.start_graph_race_name(ID,NAME)
    plot_url_place = urls[0]
    plot_url_gaps = urls[1]
    return template('embedgraph', title='Plot.ly Graph', plot_url_place=str(plot_url_place), plot_url_gaps=str(plot_url_gaps))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
