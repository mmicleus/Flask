#flask - module
#Flask - class
from flask import Flask

#we now have an instantiated
#flask variable in the app variable
app = Flask(__name__)

#this is a constructor
#the 'route' function of the app variable
#is first called
#there's complicated back-end stuff
#going on under the hood
#the '/' represents the route page
#of the website
@app.route("/")
@app.route("/home")
def home():
	return "Hello World!"

@app.route('/about')
def about():
	return 'About this app2'

#the __name__ variable is __main__
#if we run this script with python
#directly


if __name__ == '__main__':
	app.run(debug=True)