from flask import Flask
import schedule
import time

app = Flask(__name__)

from app import routes

#create query

#basically, depending on the type of frequency the user chooses, it will go into a certain type of route

@app.route('/second/')
def second():
       minutes = #sortby minutes; not sure how to write it so minutes is equal to the number the user inputs; similar thing to stuff below
       seconds = minutes * 60 #converts to seconds

@app.route('/minute/')
def minute():
       minutes = 
       seconds = minutes * 60 #converts to seconds


@app.route('/hour/')
def hour():
       hours = 
       seconds = hours * 3600 #converts to seconds

@app.route('/week/')
def week():
       weeks =
       seconds = weeks * 604800 #converts to seconds

schedule.every(seconds)seconds.do(reload)

if __name__ == "__main__":
    app.run(debug=True)
