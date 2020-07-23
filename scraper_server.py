#this runs on your local webserver
from flask import Flask, request #import main Flask class and request object
from urllib.request import urlopen # lets us request a url
from urllib.error import HTTPError
import urllib.request
from bs4 import BeautifulSoup
app = Flask(__name__) #create the Flask app

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        website = request.form.get('website')
        topic = request.form['topic']
        
        #code for webscraper, takes the information that user enters through the form
        html = urllib.request.urlopen(website).read()
        soup = BeautifulSoup(html, 'html.parser')

        for script in soup(["script", "style"]):
            script.extract()

        #takes all visible text on page
        text = soup.get_text()

        #counts number of results of topic/item on page & ignores case sensitivty
        results = text.lower().count(topic)
        
        #prints results
        answer = 'Website: ' + website + '.\n' + 'Number of results for ' + topic + ': ' + str(results) + '.'
        print(answer)

        return answer
        
    #welcome page
    return "Welcome!"

if __name__ == '__main__':
    app.run(debug=True, port=3000)