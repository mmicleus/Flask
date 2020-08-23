#flask - module
#Flask - class
from flask import Flask, render_template

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


posts = [ 
{
	'author' : 'Corey Schafer',
	'title'  :  'Blog Post 1',
	'content' : 'First Post content',
	'date_posted' : 'April 20, 2018'
},
{
	'author' : 'Jane',
	'title'  :  'Blog Post 2',
	'content' : 'Second Post content',
	'date_posted' : 'April 21, 2018'
}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts = posts)

@app.route('/about')
def about():
	return render_template('about.html')

#the __name__ variable is __main__
#if we run this script with python
#directly


if __name__ == '__main__':
	app.run(debug=True)