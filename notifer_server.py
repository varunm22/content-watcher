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
  # Assume data comes from somewhere else
  data = {
    "data": [
      {
        "id": "1",
        "website": "https://www.nytimes.com/",
        "topic": "covid",
        "frequency": "5",
      },
      {
        "id": "2",
        "website": "https://labs.codeday.org/schedule",
        "topic": "python",
        "frequency": "2",
      }]
  }
  return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=4000) 
