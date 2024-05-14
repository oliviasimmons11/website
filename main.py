from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "this would be the secret key that you make up, don't post this to github obviously"
class NameForm(FlaskForm):
   name = StringField("What is your name?", validators=[DataRequired()])
   submit = SubmitField("Submit Name")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/users'
db = SQLAlchemy(app)

#this creates a model (Sets up how data is to be added into the database)this goes under your configs
class Users(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String(100), nullable=False, unique=True)


#this creates a string to show on the screen what we've just done.
   def __repr__(self):
       return '<Name %r>' % self.name


class UserForm(FlaskForm):
   name = StringField("Name", validators=[DataRequired()])
   email = StringField("Email", validators=[DataRequired()])
   submit = SubmitField("Submit")
#we could make the email validator and email one but I haven’t tried that yet.






@app.route('/')
def index():
   return render_template('home.html', page_title='Home')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
   name = None
   form = UserForm()
   if form.validate_on_submit():
       user = Users.query.filter_by(email=form.email.data).first()
       #query the database checking for all the users that have the
       #email that have the same email as typed into the form
#return the first one that has that email (there shouldn't be any)
       #if it returns something we want to stop
       if user is None:
           user = Users(name=form.name.data, email=form.email.data)
           db.session.add(user)
           db.session.commit()
       name = form.name.data
       #now clear the form
       form.name.data = ''
       form.email.data = ''
       flash("User Added Successfully")
   our_users = Users.query.order_by(Users.email)
   return render_template("add_user.html",
       form=form,
       name=name,
       our_users=our_users)



#set up a route for name using methods (plural).
#This allows the user to GET information and POST information
@app.route('/name', methods=['GET', 'POST'])
def name():
   name = None
   #this means that the first time the user loads the page there won't be a name but once fill out the form it'll put it there
   form = NameForm() #this is using the form we created above
   #validation of the form
   if form.validate_on_submit():
       name = form.name.data
       form.name.data = ''
       #if someone submits the form then we assign that to the name variable
       #otherwise it is blank
   return render_template('name.html',
           name = name,
           form = form)


@app.route('/about')  # note the leading slash, it’s important
def about():
   return render_template('about.html', page_title='ABOUT')


@app.route('/user/<name>')
def user(name):
  favourite_food = ["Burgers", "Pizza", "Chocolate", "Sushi", "Fried Chicken", "Combination 4"]
  stuff = "This is <strong>Bold</strong>"
  return render_template('user.html', user_name=name, stuff=stuff, favourite_food=favourite_food)


if __name__ == "__main__":  
   app.run(debug=True)
