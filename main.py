from flask import Flask, url_for,request, redirect, render_template

import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def index():
    return render_template('index.html')

def empty_val(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def text_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def text_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def text_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def text_period_more_than_one(x):
    if x.count('.') <= 1:
        return True
    else:
        return False



@app.route("/signup", methods=['POST'])
def user_signup_complete():


    username = request.form['username']
    password = request.form['password']
    password_validate = request.form['vpassword']
    text = request.form['text']

    username_error = ""
    password_error = ""
    password_validate_error = ""
    text_error = ""

    err_required = "Required field"
    err_reenter_pw = "Please re-enter password"
    err_char_count = "must be between 3 and 20 characters"
    err_no_spaces = "must not contain spaces"
    
    
    if not empty_val(password):
        password_error = err_required
        password = ''
        password_validate = ''
    elif not char_length(password):
        password_error = "Password " + err_char_count
        password = ''
        password_validate = ''
        password_validate_error = err_reenter_pw
    else:
        if " " in password:
            password_error = "Password " + err_no_spaces
            password = ''
            password_validate = ''
            password_validate_error = err_reenter_pw


    if password_validate != password:
        password_validate_error = "Passwords must match"
        password = ''
        password_validate = ''
        password_error = 'Passwords must match'
            

    if not empty_val(username):
        username_error = err_required
        password = ''
        password_validate = ''
        password_error = err_reenter_pw
        password_validate_error = err_reenter_pw
    elif not char_length(username):
        username_error = "Username " + err_char_count
        password = ''
        password_validate = ''
        password_error = err_reenter_pw
        password_validate_error = err_reenter_pw
    else:
        if " " in username:
            username_error = "Username " + err_no_spaces
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw

    if empty_val(Text):
       
        if not char_length(Text):
            text_error = "Text " + err_char_count
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not text_at_symbol(text):
            text_error = "Text must contain the @ symbol"
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not text_at_symbol_more_than_one(text):
            text_error = "Text must contain only one @ symbol"
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not text_period(text):
            text_error = "Text must contain ."
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not text_period_more_than_one(text):
            text_error = "Text must contain only one ."
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        else:
            if " " in text:
                text_error = "Text " + err_no_spaces
                password = ''
                password_validate = ''
                password_error = err_reenter_pw
                password_validate_error = err_reenter_pwd

    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)


@app.route('/welcome')
def about():
    username = request.args.get('username')
    return render_template('welcome.html')

if __name__=="__main__": 
   app.run()