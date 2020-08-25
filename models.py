from flask import Flask, render_template,url_for,flash,redirect
#in the 'forms.py' file we have the 'RegistrationForm' and 'LoginForm' classes declared
from forms import RegistrationForm,LoginForm
from datetime import datetime
from blogPost import db



class User(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(20), unique = True,nullable = False)
	email = db.Column(db.String(120), unique = True,nullable = False)
	#the image and the password will be hashed
	image_file = db.Column(db.String(20),nullable = False, default = 'default.jpg')
	password = db.Column(db.String(60),nullable = False)

	#this defines how the 'print' function should display objects of type 'User'
	def __repr__():
		return f"User({self.username}), '{self.email}' , '{self.image_file})' "

	#this model will establish a relationship with the 'Post' model
	#'lazy = True' means that SQL will load the data in one go
	#this is not a column
	#this just runs an additional query to get all the posts of each user


	#Explanation
	#Let's say we have users = User(username = 'John',email = 'Marcus@gmail.com',password = '123')
	#now ,user is an instance of the 'user' class
	#user.posts will display a list of all the 'post' objects that have this user's id as their foreign key
	#post.author will  be called on objects of type 'Post' and will return the 'User' Object 
	posts = db.relationship('Post', backref = 'author',lazy = True)



#this class will be used to create a table called 'Post'
#this class is called a 'model'

class Post(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(100),nullable = False)
	#don't put paranthesis at default because you don't want to call the function
	#all you want is to pass in the function to default
	#you always want to use utc for times in databases
	date_posted = db.Column(db.DateTime,nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	#this is going to be the primary key of the user
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable =False)

	def __repr__():
		return f"Post({self.title}) {self.date_posted}"

