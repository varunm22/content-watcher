from flask import Flask
import schedule
import time

app = Flask(__name__)

from app import routes

#create query

#basically, depending on the type of frequency the user chooses, it will go into a certain type of route

query_id = {'' : {'add' : }
            '' : {'create' : }
            '' : {'delete' : }}

@app.route('/add_query' methods = ['GET,'POST'])
def add_query():
      website = request.form.get('website')
      frequency = request.form.get('frequency')
      topic = request.form.get('topic')

schedule.every(frequency)seconds.do(add_query)

@app.route('/delete_query')
def delete_query():



@app.route('/show_all')
def show_all():



if __name__ == "__main__":
    app.run(debug=True)
