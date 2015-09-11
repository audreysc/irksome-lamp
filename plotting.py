import data as d
import datetime
import plotly.plotly as py
from plotly.graph_objs import *
from collections import OrderedDict
import copy

def graph_ranks(all_runners):
    traces = []
    for runner in all_runners:
        # switched these
        y = runner.by_day.values()
        x = runner.by_day.keys()
        traces.append(Scatter(
            x=x,
            y=y,
            mode='lines+markers',
            name=runner.name,
            text=y,
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

def graph_ranks_runner(all_runners, names):
    traces = []
    for runner in all_runners:
        y = runner.by_day.values()
        x = runner.by_day.keys()
        if runner.name in names:
            print runner.name
            traces.append(Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                name=runner.name,
                text=y,
            ))
        else:
            traces.append(Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                name=runner.name,
                text=y,
                visible=False,
            ))
    data = Data(traces)
    names_list = copy.copy(names)
    final_name = ""
    if len(names_list)>1:
        final_name = names_list.pop()
        final_name = " and " + final_name
    layout = Layout(
        title='Place by Day for {name}'.format(name=" , ".join(names_list)) + final_name,
        xaxis=XAxis(
            autorange=True,
            title='Date',
        ),
        yaxis=YAxis(
            autorange=True,
            title='Place (first through last)',
        ),
    )
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='test', auto_open=False)
    return plot_url
#all_runners = d.start_graph_race('215')
#graph_ranks(all_runners)

def plotgaps(traces):
    #run_data = race_by_id(ID)
    #run_data = from_csv()
    data=Data(traces)
    layout=Layout(
        title='Frequency of Rest Length',
        xaxis=XAxis(
            title='Rest Length (Days)',
        ),
        yaxis=YAxis(
            title='Count',
        ),
    )
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Gaps', auto_open=False)
    return plot_url

def plot_bar(x, y, name):
    print x
    print y
    trace = Bar(
        x=x,
        y=y,
        name=name
    )
    return trace
