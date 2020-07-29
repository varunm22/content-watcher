#flask server set up for notifier; 
# DOES NOT SEND OR RECEIVE ANY DATA FROM OTHER SERVERS YET

from flask import Flask, request
import smtplib

app = Flask(__name__) #create the Flask app
app.secret_key = "notifier"

@app.route("/", methods=['GET', 'POST'])
def notifer():
     #if request.method == 'POST': #this block is only entered when the form is submitted
          #json = request.get_json()
          #website = json['website']
          #topic = json['topic']
          #frequency = json['frequency']
          #results = json['results']
     
          #sample queries
          queries_string = {
          "queries": [
               {
               "id": "1",
               "website": "https://www.nytimes.com/",
               "topic": "covid",
               "frequency": "5"
               },
               {
               "id": "2",
               "website": "https://www.buzzfeed.com/",
               "topic": "makeup",
               "frequency": "2"
               },
               {
               "id": "3",
               "website": "https://labs.codeday.org/schedule",
               "topic": "python",
               "frequency": "3"
               }
          ]
          }
          return jsonify(queries_string)

     #return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True, port=4000) 
