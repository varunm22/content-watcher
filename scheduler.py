from flask import Flask, request, jsonify
import time
import os, json
from apscheduler.schedulers.background import BackgroundScheduler
import requests

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

def scrape(website, topic, query_id):
    def scrape_():
        # VARUN - TODO: write code here to actually call the scraper and do what you
        # want to with the results
        url = 'http://127.0.0.1:3000/'
        scraper_data = {"website": website, "topic": topic}
        x = requests.post(url, json = scraper_data)
        query = read_data({}, "query")
        print(query_id, query)
        if str(query_id) in query and len(x.text) < 10:
            print(x.text)
            query[str(query_id)]["results"] = x.text
            write_data(query, "query")

    return scrape_

scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/add_query', methods=['GET','POST'])
def add_query():
    json = request.get_json()
    website = json['website']
    frequency = json['frequency']
    topic = json['topic']

    print(1)
    query = read_data({}, "query")
    print(2)
    query_id = read_data(1, "query_id")
    job = scheduler.add_job(func=scrape(website, topic, query_id), trigger="interval", seconds = frequency, id=str(query_id))
    query[query_id] = {'topic' : topic, 'website' : website, 'frequency' : frequency, 'results': "0"}
    query_id += 1
    write_data(query_id, "query_id")
    write_data(query, "query")

    return "Query created!"

@app.route('/delete_query', methods=['GET', 'POST'])
def delete_query():
    query = read_data({}, "query") 
    del query[query_id]
    write_data(query, "query")
    scheduler.remove_job(str(query_id))
    return "Query deleted!"

@app.route('/show_all', methods=['GET'])
def show_all():
    if request.method == 'GET':
        query = read_data({}, "query")
        return jsonify(query)

if __name__ == "__main__":
    app.run(debug=True)
