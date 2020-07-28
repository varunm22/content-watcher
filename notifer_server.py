#flask server set up for notifier; 
# DOES NOT SEND OR RECEIVE ANY DATA FROM OTHER SERVERS YET

from flask import Flask, request
import smtplib

app = Flask(__name__) #create the Flask app
app.secret_key = "notifier"

@app.route("/", methods=['GET', 'POST'])
def notifer():
     if request.method == 'POST': #this block is only entered when the form is submitted
          return "Results!"

if __name__ == "__main__":
    app.run(debug=True, port=4000) 
