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
  
    # VARUN this is just sample code i wrote for you using the read_data
    # and write_data functions I wrote above to store data. You'll need
    # to use these to create your query dict and access/modify it
    counter = read_data(1, "counter")
    query[counter] = {str(counter) :
                         {'topic' : topic,
                         'website' : website,
                         'frequency' : frequency},}
    print(counter)
    counter += 1
    write_data(counter, "counter")



    schedule.every(frequency).seconds.do(add_query)
    return "Query added!"

# VARUN: remember, all you want as an input for delete is a query id! this
# when you're taking things out of json, all you should be taking out is
# query id. If you don't understand what i mean, ask me!
@app.route('/delete_query', methods=['GET', 'POST'])
def delete_query():
#    json = request.get_json()
#    website = json['website']
#    frequency = json['frequency']
#    topic = json['topic']
    query = {}


    schedule.every(frequency).seconds.do(delete_query)
    return "Query deleted!"

#@app.route('/show_all', methods=['GET', 'POST'])
#def show_all():

if __name__ == "__main__":
    app.run(debug=True)
