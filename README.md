Simple app that lets person enter their name and get a bunch of graphs with their race stats for racery races.

Graphs:
- Trading places graph: The goal is to create a graphic that shows runners switching race positions from
day to day. 
- Rest days graph: Show how frequently people rest for 0,1,2 etc. days

The app runs with bottle and was deployed through dokku, which was running on an
EC2 AWS instance.

In development- added environment variables to the bottom of the file `$ENV/bin/activate`.

BASE_URL="racery\_api" 
PLOTLY_KEY="plotly\_key" 
PLOTLY_USER="plotly\_username"

When deployed to dokku, set environment variables with 

`dokku config:set <app_name> KEY=VALUE KEY=VALUE...`

