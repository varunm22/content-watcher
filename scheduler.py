from flask import Flask, request
import schedule
import time

app = Flask(__name__)

def read_data(variable_name):
    with open(variable_name + '.json', 'r') as f:
        value = json.load(f)
    f.close()
    return value


def write_data(value, variable_name):
    with open(variable_name + '.json', 'w') as f:
        json.dump(value, f)
    f.close()

@app.route('/add_query', methods=['GET','POST'])
def add_query():
    json = request.get_json()  
    website = json['website']
    frequency = json['frequency']
    topic = json['topic']

    # this is just sample code i wrote for you using the read_data and
    # write_data functions I wrote above to store data. You'll need to
    # use these to create your query dict and access/modify it
    if os.path.exists("counter.json"):
        counter = read_data()
    else:
        counter = 1
    print(counter)
    counter += 1
    write_data(counter)

    schedule.every(frequency).seconds.do(add_query)

@app.route('/delete_query', methods=['GET', 'POST'])
def delete_query():
    json = request.get_json()
    website = json['website']
    frequency = json['frequency']
    topic = json['topic']

#same as add but it decreases counter
    if os.path.exists("counter.json"):
        counter = read_data()
    else:
        counter = 1
    print(counter)
    counter -= 1
    write_data(counter)

    schedule.every(frequency).seconds.do(delete_query)

#@app.route('/show_all')
#def show_all():

if __name__ == "__main__":
    app.run(debug=True)
