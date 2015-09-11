import os
from bottle import run, template, get, post, request, redirect

import plotly.plotly as py
from plotly.graph_objs import *

import data as d
import plotting as p
from collections import OrderedDict
import json

# Development: Set at bottom of $ENV/bin/activate
# Production: Set in dokku app config
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
    NAME1 = request.forms.get('NAME1')
    NAME2 = request.forms.get('NAME2')
    NAME3 = request.forms.get('NAME3')
    NAME4 = request.forms.get('NAME4')
    NAMES = filter(lambda name: name!= '' , [NAME1, NAME2, NAME3, NAME4])
    print NAMES
    urls = d.start_graph_race_name(ID,NAMES)
    plot_url_place = urls[0]
    plot_url_gaps = urls[1]
    return template('embedgraph', title='Plot.ly Graph', plot_url_place=str(plot_url_place), plot_url_gaps=str(plot_url_gaps))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
