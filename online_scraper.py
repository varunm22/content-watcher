#this code currently connects the scraper with the frontend query entry

from flask import Flask, redirect, url_for, render_template, request, session
from urllib.request import urlopen # lets us request a url
from urllib.error import HTTPError
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__) #create the Flask app
app.secret_key = "webscraper"

@app.route("/")
def scraper():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        website = request.form.get('website')
        topic = request.form.get('topic')
        
        #code for webscraper, takes the information that user enters through the form
        html = urllib.request.urlopen(website).read()
        soup = BeautifulSoup(html, 'html.parser')

        for script in soup(["script", "style"]):
            script.extract()

        #takes all visible text on page
        text = soup.get_text()

        #counts number of results of topic/item on page & ignores case sensitivty
        results = str(text.lower().count(topic))
        
        #prints results
        #answer = 'Website: ' + website + '.\n' + 'Number of results for ' + topic + ': ' + results + '.'

        return '''<p> Website: {}</p>
                <p> Search Term: {}</p>
                <p> Number of Results: {}</p>'''.format(website, topic, results)
        
    #form shown on webserver/site that prompts user to enter information
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 
