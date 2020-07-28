from flask import Flask
import schedule
import time

app = Flask(__name__)

from app import routes

#create query

#query id: depending on the id (which is a number), it adds, creates, or deletes

#query_id = {'0' : {'add' : "h",}, 
#            '1' : {'create' : "j",},
#            '2' : {'delete' : "l",},}

@app.route('/add_query', methods=['GET','POST'])
def add_query():
      website = request.form.get('website')
      frequency = request.form.get('frequency')
      topic = request.form.get('topic')

schedule.every(frequency).seconds.do(add_query)

#@app.route('/delete_query')
#def delete_query():



#@app.route('/show_all')
#def show_all():

if __name__ == "__main__":
    app.run(debug=True)
