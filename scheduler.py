from flask import Flask
import schedule
import time

app = Flask(__name__)

from app import routes

#create query

#basically, depending on the type of frequency the user chooses, it will go into a certain type of route

front_end = {'query_id' :
              'frequency' : }

@app.route('/second/')
def second():
       seconds = front_end['frequency']



@app.route('/minute/')
def minute():
       minutes = front_end['frequency']
       seconds = minutes * 60 #converts to seconds


@app.route('/hour/')
def hour():
       hours = front_end['frequency']
       seconds = hours * 3600 #converts to seconds

@app.route('/week/')
def week():
       weeks = front_end['frequency']
       seconds = weeks * 604800 #converts to seconds

schedule.every(seconds)seconds.do(reload)

if __name__ == "__main__":
    app.run(debug=True)
