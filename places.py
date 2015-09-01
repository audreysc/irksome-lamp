import data as d
import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from collections import OrderedDict

def graph_ranks(all_runners):
    credentials = tls.get_credentials_file()
    py.sign_in(credentials['username'], credentials['api_key'])
    traces = []
    for runner in all_runners:
        runner.by_day = OrderedDict(sorted(runner.by_day.items(), key=lambda t: int(t[0])))
        print runner.name
        x = runner.by_day.values()
        y = runner.by_day.keys()
        print x
        print y
        traces.append(Scatter(
            x=x,
            y=y,
            mode='lines+markers',
            name=runner.name,
            text=x,
        ))
    data = Data(traces)
    layout = Layout( 
        xaxis=XAxis(
            autorange=True,
        ),
        yaxis=YAxis(
            autorange=True,
        ),
    )
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Trading Places')
