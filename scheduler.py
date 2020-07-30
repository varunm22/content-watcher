from flask import Flask, request
import schedule
import time
import os, json

app = Flask(__name__)

def read_data(starting_value, variable_name):
    variable_path = variable_name + '.json'
    if os.path.exists(variable_path):
        with open(variable_path, 'r') as f:
            print(variable_path)
            value = json.load(f)
        f.close()
        return value
    else:
        return starting_value

def write_data(value, variable_name):
    with open(variable_name + '.json', 'w') as f:
        json.dump(value, f)
    f.close()

@app.route('/add_query', methods=['GET','POST'])
def add_query():
    query = {}
    json = request.get_json()
    website = json['website']
    frequency = json['frequency']
    topic = json['topic']

    query_id = read_data(1, "query_id")
    query[query_id] = {'topic' : topic, 'website' : website, 'frequency' : frequency}
    query_id += 1
    write_data(query_id, "query_id")

    schedule.every(frequency).seconds.do(add_query).tag('create')
    return "Query created!"

@app.route('/delete_query', methods=['GET', 'POST'])
def delete_query():

    del query['query_id']
    schedule.clear('create')
    return "Query deleted!"

@app.route('/show_all', methods=['GET', 'POST'])
def show_all():
    return query

if __name__ == "__main__":
    app.run(debug=True)
