import data as d
import datetime
import plotly.plotly as py
from plotly.graph_objs import *
from collections import OrderedDict

def graph_ranks(all_runners):
    traces = []
    for runner in all_runners:
        x = runner.by_day.values()
        y = runner.by_day.keys()
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
    plot_url = py.plot(fig, filename='test')
    return plot_url

def graph_ranks_runner(all_runners, name):
    traces = []
    for runner in all_runners:
        x = runner.by_day.values()
        y = runner.by_day.keys()
        if runner.name == name:
            traces.append(Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                name=runner.name,
                text=x,
            ))
        else:
            traces.append(Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                name=runner.name,
                text=x,
                visible=False,
            ))
    data = Data(traces)
    layout = Layout(
        title='Place by Day for {name}'.format(name=name),
        xaxis=XAxis(
            autorange=True,
            title='Place (first through last)',
        ),
        yaxis=YAxis(
            autorange=True,
            title='Days from start of race',
        ),
    )
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='test', auto_open=False)
    return plot_url
#all_runners = d.start_graph_race('215')
#graph_ranks(all_runners)