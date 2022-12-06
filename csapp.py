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
all_users = [] # Put all unique users in this list, get inside the tuple
all_users2 = "" # Use to convert into string to send to javascript
for i in all_username:
    all_users.append(i[0]) # get values in tuple
#print(all_users)

for i in all_users:
    x = i + " " # space after every user
    all_users2 += x
#print(all_users2)
# Note for teacher: We are converting all_users2 into 
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
        if(False):
            message = {'greeting':'Please have an unique Email'}
            print('false')
            return jsonify(message)
        else:
            print('Signed up: ' + req['username'])
            
                
    return render_template('signup.html', userz=['s', 'b'])

    

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

    