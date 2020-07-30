#flask server set up for notifier; 
# DOES NOT SEND OR RECEIVE ANY DATA FROM OTHER SERVERS YET

from flask import Flask, request, render_template, json, jsonify

app = Flask(__name__) #create the Flask app
app.secret_key = "notifier"

@app.route('/')
def index():
  return render_template('queries.html')

@app.route('/index_get_data')
def queries():
  List = []
  #Scheduler outputs data like this:
  scraper_data = {1:{"website": "https://www.nytimes.com/", "topic": "covid", "frequency": "5"}, 2:{"website": "https://labs.codeday.org/schedule", "topic": "python", "frequency": "2"}}
  for key, value in scraper_data.items():
      value["query_id"] = key
      List.append(value)

  data = {
    "data": List
  }
  return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=4000) 
