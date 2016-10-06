Simple app that lets person enter their name and get a bunch of graphs with their race stats for racery races.

Graphs are created and displayed using Plotly, there are two graphs currently:
- Trading places graph: The goal is to create a graphic that shows runners switching race positions from
day to day. 
- Rest days graph: Show how frequently people rest for 0,1,2 etc. days

The app runs with bottle and was deployed through dokku, which was running on an
EC2 AWS instance (it is not currently deployed).

In development- added environment variables to the bottom of the file `$ENV/bin/activate`.

BASE_URL="racery\_api" 
PLOTLY_KEY="plotly\_key" 
PLOTLY_USER="plotly\_username"

When deployed to dokku, set environment variables with 

`dokku config:set <app_name> KEY=VALUE KEY=VALUE...`

This is how the form screen looks :

![Form](/get_your_racery_stats.png)

This is how the graphs look:

![Comparison Graphs](/comparison_graphs.png)
