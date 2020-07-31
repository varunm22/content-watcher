#this is a separate webserver for only query entries that works independently of itself, 
#a success message will appear when a post request is successfully made

from flask import Flask, redirect, url_for, render_template, request, session
import requests

app = Flask(__name__) #create the Flask app
app.secret_key = "queryentry"

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        website = request.form.get('website')
        topic = request.form.get('topic')
        frequency = int(request.form.get('frequency'))
        print("sssss", website, topic, frequency)
        url = 'http://127.0.0.1:5000/add_query' #sends information to scheduler server
        myobj = {'website': website, 'topic': topic, 'frequency': frequency}
        x = requests.post(url, json = myobj)
        return "Success! Information entered!" 
    #form shown on webserver/site that prompts user to enter information
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001) 
