from flask import Flask, render_template, request, flash, redirect, url_for, make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required, UserMixin, LoginManager
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # initialize flask sql database
db = SQLAlchemy(app) # initialize flask sql database, db

# Create FLASK SQL CLASSES

class Opportunities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_tasks = db.Column(db.String(10000), nullable=False)
    firstName = db.Column(db.String(150), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    datetime = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    money_paid = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    opportunities = db.relationship('Opportunities')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return '<h1>Home</h1>'
# Below are test variables
user = 'biswas'
email = 'biswassudiptto@gmail.com'
# GRAB ALL THE DATA FROM THE USERNAME COLUMN
all_username = User.query.with_entities(User.username).all() # cann do all_username[0] to get individual data
all_users2 = "" # Use to convert into string to send to javascript, this is because you cannot send arrays with letters into JavaScript
for i in all_username:
    x = i[0] + " " # make sure it's out of the tuple form
    all_users2 += x
print(all_users2)

# GRAB ALL THE DATA FROM THE EMAIL COLUMN
all_emails = User.query.with_entities(User.email).all()
all_email = ""
for i in all_emails:
    x = i[0] + " "
    all_email += x
#print(type(all_email)) // WORKS!
#print(all_email)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    x = ['s', 'd']
    #all_users = User.query.filter().all() 
    
    if request.method == 'POST':
        req = request.get_json() # dictionary. get the json data being sent and conver to python dictionary
        print(req)
        print('works')
        print(req['email'])
        print(req['username'])
        
        print('Signed up: ' + req['username'])
        #return {"message": "Signed Up!"}
            
                
    return render_template('signup.html', userz=all_users2, mailxs=all_email)

    

#@app.route('/signup')
#def signup():
#    return render_template('signup.html')

"""""""""
@app.route('/signup_method', methods=['POST'])
def signup_method():
    req = request.get_json() # dictionary. get the json data being sent and conver to python dictionary
    print(req)
    if len(req) > 1:
        print('works')
        return redirect(url_for('home'))
    res = make_response(jsonify({"messsage":"JSON"}), 200)
    return res """""""""

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

    