from flask import Flask, request
import time
import os, json
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def read_data(starting_value, variable_name):
    variable_path = variable_name + '.json'
    if os.path.exists(variable_path):
        with open(variable_path, 'r') as f:
            value = json.load(f)
        f.close()
        return value
    else:
        return starting_value

def write_data(value, variable_name):
    with open(variable_name + '.json', 'w') as f:
        json.dump(value, f)
    f.close()

def scrape(website, topic):
    def scrape_():
        # VARUN - TODO: write code here to actually call the scraper and do what you
        # want to with the results
        pass
    return scrape_

scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/add_query', methods=['GET','POST'])
def add_query():
    query = {}
    json = request.get_json()
    website = json['website']
    frequency = json['frequency']
    topic = json['topic']

    schedule.every(frequency).seconds.do(test).tag('create')
    job = scheduler.add_job(func=scrape(website, topic), trigger="interval", seconds = frequency)

    query_id = read_data(1, "query_id")
    query[query_id] = {'topic' : topic, 'website' : website, 'frequency' : frequency, 'job': job}
    query_id += 1
    write_data(query_id, "query_id")

    return "Query created!"

@app.route('/delete_query', methods=['GET', 'POST'])
def delete_query():
    # VARUN - TODO: you'll need to read the query variable from somewhere!
    # VARUN - TODO: I don't think this is the right way to access the query you want.
    # get that working then I'll help with deleting the schedule
    query = read_data(0, "query") 
    del query[query_id]
    write_data(query, "query")
    return "Query deleted!"

@app.route('/show_all', methods=['GET', 'POST'])
def show_all():
    return query

if __name__ == "__main__":
    app.run(debug=True)
