#flask server set up for notifier/query table 

import json
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__) #create the Flask app
app.secret_key = "notifier"

@app.route('/')
def index():
  return render_template('queries.html')

@app.route('/index_get_data')
def queries():
  url = 'http://127.0.0.1:5000/show_all' #sends post request to scheduler
  scraper_data = json.loads(requests.get(url).text)
  
  List = []
  #Scheduler outputs data like this as a dictionary:
  for key, value in scraper_data.items():
      value["query_id"] = key
      List.append(value)

  data = {
    "data": List
  }
  return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=4000) 
