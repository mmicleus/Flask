from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email


#before implementing these 2 forms we need to include a secret key in the forms
#this key will protect against modifying cookies and cross-site request forgery attacks


#this class inherits from the Flask Form class
class RegistrationForm(FlaskForm):
	#'validators' is named parameter of the 'StringField' function
	#it takes in a list of objects that we also have to import
	#Data_Required will prevent the generated form from being empty
	#the 'Length' object will make sure the nr of characters is between min and max

	#username represents an input field that requires data to be inputted and the data should
	#have between min and max characters
	#the first string will be the label
	username = StringField('Username',validators = [DataRequired(), Length(min = 2, max = 20)] )
	#Email() will make sure it's a valid field
	#email = StringField('Email',validators = [DataRequired(), Email() ])
	password = PasswordField('Password' ,validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password' ,validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


#this class inherits from the Flask Form class
class LoginForm(FlaskForm):
	#'validators' is named parameter of the 'StringField' function
	#it takes in a list of objects that we also have to import
	#Data_Required will prevent the generated form from being empty
	#the 'Length' object will make sure the nr of characters is between min and max
	username = StringField('Username',validators = [DataRequired(), Length(min = 2, max = 20)] )
	#Email() will make sure it's a valid field
	password = PasswordField('Password', validators = [DataRequired()])
	#this will allow the user to stay logged in for a while using a cookie
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')



