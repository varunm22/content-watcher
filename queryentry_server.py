#this is a separate webserver for only query entries that works independently of itself, 
#a success message will appear when a post request is successfully made

from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__) #create the Flask app
app.secret_key = "queryentry"

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        website = request.args.get('website')
        topic = request.args.get('topic')
        url = 'http://127.0.0.1:3000/'
        myobj = {'website': website, 'topic': topic}
        x = requests.post(url, data = myobj)
        return "Success! Information entered!" 
    #form shown on webserver/site that prompts user to enter information
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001) 
