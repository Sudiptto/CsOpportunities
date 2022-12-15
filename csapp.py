from flask import Flask, render_template, request, flash, redirect, url_for, make_response, jsonify
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required, UserMixin, LoginManager
from sqlalchemy.sql import func
import requests
import json
from password import *
from flask_sqlalchemy import SQLAlchemy
import os
 
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # initialize flask sql database
db = SQLAlchemy(app) # initialize flask sql database, db


# configure the email

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'csopp4all@gmail.com' # senders username 
app.config['MAIL_PASSWORD'] = passwordd
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) # initialize flask mail

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
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

xy = ""
@app.route('/', methods=['POST', 'GET'])
def login():
  
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first() # query through the email
        if user: # if user exists 
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                global login_value
                login_value = "Logged"
                #xy += "Logged"
                flash('Logged in successfully!', category='success')
                return redirect(url_for('home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error') 
    return render_template('login.html')

# Below are test variables

# GRAB ALL THE DATA FROM THE USERNAME COLUMN
all_username = User.query.with_entities(User.username).all() # cann do all_username[0] to get individual data
all_users2 = "" # Use to convert into string to send to javascript, this is because you cannot send arrays with letters into JavaScript
for i in all_username:
    x = i[0] + " " # make sure it's out of the tuple form
    all_users2 += x
#print(all_users2)

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
        #print(req)
        print('works')
        #print(req['email'])
        #print(req['username'])
        #print('Signed up: ' + req['username'])
        #return {"message": "Signed Up!"}
        username = req['username']
        email = req['email']
        first_name = req['Fname']
        last_name = req['Lname']
        password = req['password']

        new_user = User(username=username, password=generate_password_hash(password, method = "sha256"), email=email, first_name=first_name, last_name=last_name)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        #return 'sf', 200
            
               # , userz=all_users2, mailxs=all_email
    return render_template('signup.html', userz=all_users2, mailxs=all_email)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Create routes after making loggin the users
@app.route('/home')
@login_required
def home():
    return render_template('index.html', user=current_user)

@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    if request.method == 'POST':
        req = request.get_json()
        title = req['title']
        duration = int(req['duration'])
        date = req['date']
        paid = int(req['paid'])
        description = req['description']

        print('works')
        #print(type(paid))
        #print(title + ' ' + str(duration) + ' ' + date + ' ' + str(paid) + ' ' + description)

        # add to database
        #print(current_user.username + ' ' + current_user.id)
        new_opp = Opportunities(data_tasks=description, firstName = current_user.first_name, lastName = current_user.last_name, title=title, email=current_user.email, datetime=date, duration=duration, money_paid=paid, user_id=current_user.id)
        db.session.add(new_opp)
        db.session.commit()
    return render_template('upload.html', user=current_user)

@app.route('/opportunities')
def opportunities():
    all_opportunities = Opportunities.query.filter().all() # filter the database for every opportunity 
    opp = all_opportunities[::-1] # reverse the list 
    return render_template('opportunities.html', user=current_user, opp = opp)

# this will delete the opportunites
# get the data from javascript, it will get the opportunity id and than it will check if the note exists
@app.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Opportunities.query.get(noteId)
    if note: # if the note exists
        if note.user_id == current_user.id: # if the note user id matches the user id of the person that is currently logged in
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@app.route('/stackproblems')
@login_required
def stackproblems():
    # get the data that is in that link 
    set1 = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    return render_template('stack.html', user=current_user, items=set1.json()['items'], x=0)


@app.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    # start with subject
    # the data below comes from javascript
    if request.method == 'POST':
        # the hey is the subject
        req = request.get_json()
        subject = req['subject']
        type_of_question = req['type_problem']
        description = req['description'] 
        # send to mail
        msg = Message(subject, sender="noreplycs.com", recipients=['csopp4all@gmail.com'])


        """msg.body = "Type of question: " + type_of_question + ", Description: " + description + ", Written by: " + current_user.email + " First name: " + current_user.first_name + " Last name: " + current_user.last_name """
        
        color1  = 'white'
        bg_color = 'black'
        #msg.html = "<h1>This is a test email from Flask-Mail</h1>"
        msg.html = "<p style='color: white; background-color: black; font-size: 25px; '>Type of Question: <strong> " + type_of_question + " </strong> <br> Description: "+ description +" <br> Written By: " + current_user.email + "<br> Full Name: " + current_user.first_name + " " + current_user.last_name + "</p>"
        
        mail.send(msg)
        return "Send email"
    return render_template('contact.html')
"""""""""
print(xy)
if xy == "Logged":
    @app.route('/home')
    def home():
        return render_template('index.html')
else:
    @app.route('/nlogin')
    def nlogin():
        return '<h1>Your not logged in</h1>'
    """""""""

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
    app.run()

    