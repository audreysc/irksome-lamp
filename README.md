Simple app that lets person enter their name and get a bunch of graphs with their
stats.

Graphs:
- Trading places graph: The goal is to create a graphic that shows runners switching race positions from
day to day. 
- Rest days graph: Show how frequently people rest for 0,1,2 etc. days
- ...

The app runs with bottle and is deployed through dokku, which is running on an
EC2 AWS instance.

In development- added environment variables to the bottom of the file `$ENV/bin/activate`. They
are in `dokku_config_vars` for local reference.

BASE_URL="racery\_api" 
PLOTLY_KEY="plotly\_key" 
PLOTLY_USER="plotly\_username"

When deployed to dokku, set environment variables with 

`dokku config:set <app_name> KEY=VALUE KEY=VALUE...`


## Resources

### Django:
http://www.in4it.io/blog/Your-Own-Platform-as-a-Service-in-5-steps-for-free-with-dokku
http://www.xorcode.com/2013/07/28/running-node-js-with-dokku-on-an-ubuntu-instance/
https://realpython.com/blog/python/deploying-a-django-app-on-dokku/

### Bottle (Python microframework)
http://bottlepy.org/docs/dev/tutorial.html#quickstart-hello-world
https://github.com/mjhea0/bottle-plotly-python/tree/master/bottle
http://www.marginhound.com/bottle-py-resources/
