# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 14:43:59 2015
@author: Audrey
"""
import datetime
import csv
import urllib2
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from collections import OrderedDict

class Race:
    
    def __init__(self, name):
        self.name = name
        self.runs = []
        self.runners = []
        self.distance = 0
        
    def add_runner(self, runner):
        self.runners.append(runner)
        
    def add_run(self, run):
        self.runs.append(run)
    
    def race_distance(self, distance):
        self.distance = distance
        
    def get_runners(self):
        all_runners = []
        for run in self.runs:
            all_runners.append(run.name)
        self.runners = set(all_runners)
        #sort(self.runs, key = attrgetter('age'))
        return sorted(self.runners)    
        
    def __repr__(self):
        return self.name
        
    def __cmp__(self, other):
        if (self.name < other.name):
            return -1
        if (self.name > other.name):
            return 1
        else:
            return 0
    
class Runner:
    
    def __init__(self, name):
        self.name = name
        self.runs = []
        self.median = 0 #median
        self.races = [] #list of races
        self.num = 0 #number of races
        self.total = 0 #total miles
        self.count = 0 #count of runs
        self.avg = 0 #average mileage/run
        self.dur = 0 #duration
        self.mpd = 0 #miles/total days
        self.rpd = 0 #runs/total days
        self.by_day = {}
        self.gap_dict = {}

    def add_run(self, run):
        self.runs.append(run)

    def make_data(self):
        self.avg_miles()
        self.num_races()
        self.running_time()
        self.frequencies()

    def frequencies(self):
        if (self.dur != 0):
            mpd = self.total/self.dur
            rpd = float(self.count)/self.dur
            self.mpd = mpd
            self.rpd = rpd

    def avg_miles(self):
        run_distances = []
        miles = 0.00
        count = 0
        counted = []
        for run in self.runs:
            if run.date not in counted:
                counted.append(run.date)
                miles += float(run.distance)
                count += 1
                run_distances.append(run.distance)
        self.median = np.median(run_distances)
        print self.median
        self.count = count
        self.total = miles
        self.avg = miles/count
        return miles/count

    def num_races(self):
        races = 0
        race_names = []
        for run in self.runs:
            if run.race not in race_names:
                races += 1
                race_names.append(run.race)
        self.num = races
        self.races = race_names
        return races 

    def running_time(self):
        FIRST = self.runs[0]
        LAST = self.runs[-1]
        x = LAST.date - FIRST.date
        self.dur = x.days
        return self.dur

        
    def __cmp__(self, other):
        
        if (self.name < other.name):
            return -1
        if (self.name > other.name):
            return 1
        else:
            return 0

class Run:
    
    miles = True
    
    def __init__(self, race, name, date, distance):
        self.race = race
        self.name = name.lower()
        self.date = date
        self.distance = distance
        
        #make these point to the class objects not strings
             
    def make_date(self):        
        date_time = self.date.split(' ')
        date_time = filter(lambda x: x.strip(' ')!='', date_time)
        d = date_time[0].split('-')
        time = date_time[1] #time, unused for now
        self.date = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    
    def miles(self):
        self.distance = self.distance*(0.000621371)
        
    def kilometers(self):
        self.distance = self.distance/1000
        
    def get_runner(self):
        return self.name
        
    def race(self):
        """race that run is in"""
        return self.race
    
    def toString(self):
        string = self.race + self.name + str(self.date) + str(self.distance)
        return string
        
    #def __repr__(self):
    #    string = self.race + self.name + str(self.date) + str(self.distance)
    #    return string
        
    def __cmp__(self, other):
        '''runs are compared by date'''
        if (self.date < other.date):
            return -1
        if (self.date > other.date):
            return 1
        else:
            return 0

class Data:
    dataFile = 'submissions.csv'
    #pass true if you want to read from URL
    #if true, extra ' ' infront of time needed
    newFile = False
    miles = True
    x = []
    
    def __init__(self, newFile, miles):
        '''boolean newFile and miles. runs, races, and runners are lists that hold the raw data information'''
        self.newFile = newFile
        self.miles = miles
        self.runs = []
        self.races = []
        self.race_names = []
        self.runners = []
        self.runner_names = []
        
    def read_data(self, **kwargs):
        #read from URL
        for key, value in kwargs.items():
            if key == 'dataFile':
                dataFile = value
            if key == 'url':
                url = value
            print key , value
        if (self.newFile == True):
            print 'reading from url to csv'
            csv_writer = open(dataFile, 'wb')
            print "Starting to read from url"
            csv_writer.write(urllib2.urlopen(url).read())
            csv_writer.close()
            print "Done reading from url"
        with open(dataFile, 'rb') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                this_run = Run(row[0], row[1].strip(' '), row[2], float(row[3]))
                if (self.miles == True):
                    this_run.miles()
                this_run.make_date()
                self.runs.append(this_run)
                self.people_list(this_run)
                self.race_list(this_run)
                #print this_run.toString()
            print 'done reading in file'
            #print 'Races: \n' + self.print_list(self.race_names)
            #print 'Runners: \n' + self.print_list(self.runner_names)

    def race_runners(self):
        for race in self.races:
            print race.get_runners()
    
    def make_lists(self, this_run):
        self.people_list(this_run)
        self.race_list(this_run)

    def race_list(self, this_run):
        """returns a list of races"""
        for race in self.races:
            if (race.name == str(this_run.race)):
                race.add_run(this_run)
                race.add_runner(this_run.get_runner())
        if str(this_run.race) not in self.race_names:
            this_race = Race(this_run.race)
            self.races.append(this_race)
            self.race_names.append(this_race.name)
            this_race.add_run(this_run)
            
        
    def people_list(self, this_run):
        """returns a list of people"""
        for runner in self.runners:
            if (runner.name == str(this_run.name)):
                runner.add_run(this_run)
        if str(this_run.name) not in self.runner_names:
            this_runner = Runner(this_run.name)
            self.runners.append(this_runner)
            self.runner_names.append(this_runner.name)
            this_runner.add_run(this_run)
    
    def print_list(self, x):
        to_string = ''
        n = 1
        x = sorted(x)
        for i in range(1, len(x)):
            to_string += str(n) + '. ' + x[i] + '\n'
            n = n+1
        return to_string
     
    def get_runner(self, x):
        for runner in self.runners:
            if (runner.name == x):
                #print runner.runs
                return runner
 
    def plot_gaps(self, *args):
        runner_list = []
        if (args > 0):
            runner_list = args
        else:
            runner_list = self.runner_names
        for runner in self.runners:
            if runner.name in runner_list:
                self.runner_gaps(runner)
    
    def runner_gaps(self, runner):
        print runner.name
        gaps = []
        #gap_dict = dict.fromKeys([range(10)])
        sorted(runner.runs, key=lambda run: run.date)
        print runner.runs
        for i in range(0, len(runner.runs)-1):
            current_run = runner.runs[i]
            next_run = runner.runs[i+1]
            rest = (next_run.date - current_run.date).days
            gaps.append(rest)
        gap_keys = (sorted(set(gaps)))
        print gap_keys
        #runner.gap_dict = dict.fromkeys(sorted(set(gaps)), None)
        for k in gap_keys:
            runner.gap_dict[k] = gaps.count(k)
            print str(k) + ': ' + str(runner.gap_dict[k])
    
    def graph_gaps(self, selected): 
        found = False
        runner = ''
        for r in self.runners:
            if (selected == r.name):
                runner = r
                found = True
                x = dict.keys(runner.gap_dict)
                y = dict.values(runner.gap_dict)
                trace = plot_now(x, y)
                return trace
        if (found == False):
            print selected + 'was not found.'
    
def plot_now(x, y):
    print x
    print y
    trace = Bar(
        x=x,
        y=y
    )
    return trace

def main(**kwargs):
    newFile = False
    for key, value in kwargs.items():
        if key == 'dataFile':
            dataFile = value
        if key == 'url':
            url = value
        if key == 'newFile':
            newFile = value
    try:
        credentials = tls.get_credentials_file()
    except:
        ## except credentials error and print for them to enter something
        credentials = {}
        credentials['username'] = raw_input("Plotly Username: ") ## get username
        credentials['api_key'] = raw_input("api key: ") ### get password
    try:
        py.sign_in(credentials['username'], credentials['api_key']) 
    except:
        print "was not able to sign into plotly"
        print "let's read some data"        
    #data object
    t = Data(newFile, True)
    #read from file
    t.read_data(**kwargs)
    return t

def race_by_id(ID):
    t = main(newFile=True, dataFile='submissions.csv', url='http://racery.com/api/list_submissions?race_id={ID}'.format(ID=ID))
    return t
def race_by_id(ID):
    t = main(newFile=True, dataFile='submissions.csv', url='http://racery.com/api/list_submissions?race_id={ID}'.format(ID=ID))
    return t

def tri_tech():
    t = main(newFile=True, dataFile='submissions.csv', url='http://racery.com/api/list_submissions?race_id=215')
    return t

def from_csv():
    t = main(newFile=False, dataFile='submissions.csv')
    return t

def empty_data():
    t = Data(False, True)
    return t

def by_date(run_data, cutoff):
    # Builds data object with runs in specifed date range
    build_data = empty_data()
    runs = filter(lambda x: x.date < cutoff, run_data.runs)
    build_data.runs = runs 
    map(lambda x:build_data.make_lists(x), build_data.runs)
    return build_data

def iter_dates(run_data):
    data_min = min(run_data.runs, key=lambda x:x.date).date
    data_max = max(run_data.runs, key=lambda x:x.date).date + datetime.timedelta(days=1)
    data_by_day = {}
    all_runners = run_data.runners
    race_order = []
    date_range = (data_max - data_min).days
    for d in range(date_range):
        day = data_min + datetime.timedelta(days=d)
        ds = str(d)
        today_runners = by_date(run_data,day).runners
        for runner in all_runners:
            r = filter(lambda a: a.name==runner.name, today_runners)
            print r
            if len(r)>0:
                (r[0]).make_data()
                day_total = r[0].total
                runner.by_day[ds] = r[0].total
                print r[0].total
            else:
                get_prev = str(d - 1)
                runner.by_day[ds] = runner.by_day[get_prev] if get_prev in runner.by_day.keys() else 0
        #for runner in all_runners:
        data_by_day[ds] = list({runner.name: runner.by_day[ds]} for runner in all_runners)
        data_by_day[ds] = reduce(lambda x,y: dict(x.items() + y.items()), data_by_day[ds])
    return all_runners, data_by_day
    
def daily_ranking(all_runners, run_data, data_by_day):
    data_min = min(run_data.runs, key=lambda x:x.date).date
    data_max = max(run_data.runs, key=lambda x:x.date).date + datetime.timedelta(days=1)
    date_range = (data_max - data_min).days
    day_ranks = {}
    for d in range(date_range):
        day = data_min + datetime.timedelta(days=d)
        ds = str(d)
        ranks = sorted(data_by_day[ds], key=lambda x : data_by_day[ds][x], reverse=True)
        day_ranks[ds] = dict(list((i+1, ranks[i]) for i in range(len(ranks))))
        for ra in day_ranks[ds].keys():
            name = day_ranks[ds][ra]
            runner = filter(lambda a: a.name==name, all_runners)
            runner[0].by_day[ds] = ra
    ## Order runner dictionaries
    for runner in all_runners:
        runner.by_day = OrderedDict(sorted(runner.by_day.items(), key=lambda t: int(t[0])))
    return all_runners, day_ranks

# Can't use Data() because class is named that
# Bar Graph that plots frequencies of rest duration.
def plotgaps(ID, NAME):
    #run_data = race_by_id(ID)
    run_data = from_csv()
    run_data.plot_gaps(NAME)
    trace = run_data.graph_gaps(NAME)
    #data=Data([trace])
    layout=Layout(
        title='Frequency of rest length',
        xaxis=XAxis(
            title='Rest Length',
        ),
        yaxis=YAxis(
            title='Count',
        ),
    )
    #fig = Figure(data=data, layout=layout)
    return trace, layout

def start_graph_race_name(ID, NAME):
    print NAME
    run_data = race_by_id(ID)
    runner = run_data.get_runner(NAME)
    d = iter_dates(run_data)
    all_runners = d[0]
    data_by_day = d[1]
    dr = daily_ranking(all_runners, run_data, data_by_day)
    all_runners = dr[0]
    day_ranks = dr[1]
    return all_runners

def start_graph_race(ID):
    run_data = race_by_id(ID)
    d = iter_dates(run_data)
    all_runners = d[0]
    data_by_day = d[1]
    dr = daily_ranking(all_runners, run_data, data_by_day)
    all_runners = dr[0]
    day_ranks = dr[1]
    return all_runners

def start_graph():
    run_data = from_csv()
    d = iter_dates(run_data)
    all_runners = d[0]
    data_by_day = d[1]
    dr = daily_ranking(all_runners, run_data, data_by_day)
    all_runners = dr[0]
    day_ranks = dr[1]
    return all_runners
