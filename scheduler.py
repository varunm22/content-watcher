from flask import Flask render_template render_Backend
import schedule
import time



app = Flask(__name__)

@app.route('/') #end of basic Flask stuff





#old stuff basically loops through everything from 0 to states seconds
def scraper():
    return render_Backend('scraper.py') #calls scraper

def index():
    return render_template('index.html') #setiing up the html

def reload():
    webbrowser.open_new_tab(url)

schedule.every(a)seconds.do(reload)#function



#n = [] # empty list to hold numbers

#m = 0
#while m >= 0:
#    n = n.append(str(m))
#    m += 1 #creates an array with all positive integers

#should keep in mind that frequency will be kept in seconds
#def frequency(a):
#    for x in n:
        #if keyword is in within this frequency, print 'Yes'
        #if not, print 'No'
        #this loop will loop through all seconds from 0 to the user's stated times