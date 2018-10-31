from flask import Flask, request, redirect, render_template
import os
import jinja2
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/' , methods=['POST', 'GET'])
def display_user_signup_form():
    return render_template('base.html')

def is_filled(val):
    if val != "":  
        return True  
    else:  
        return False  

def no_whitespace(val):
    whitespace = " "
    if whitespace not in val:
        return True
    else:
        return False

def validate_text(val):

    valid_text = re.compile("[a-zA-Z0-9_]+\.?[a-zA-Z0-9_]+@[a-z]+\.[a-z]+")
    if valid_text.match(val):
        return True
    else:
        return False

@app.route("/validate-form", methods=['POST'])
def validate():

    username_input = request.form['username']  
    password_input = request.form['password']  
    verify_input = request.form['verify']  
    text_input = request.form['email']  

    username_error = ""  
    password_error = ""  
    verify_error = ""  
    text_error = ""  

    if not username_error and not password_error and not verify_error and not text_error:  # if we don't have any error messages:
        return render_template("welcome.html", username=username_input)
    else:
        return render_template ("signup.html",
        username_input=username_input,
        text_input=text_input,
        username_error=username_error, password_error=password_error, verify_error=verify_error, text_error=text_error)


@app.route('/welcome.html')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()