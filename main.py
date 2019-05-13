from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify_password']
        email = request.form['email']

        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""

    # Do checks
        if username == username_error:
            username_error = "This field cannot be left blank"
        else:
            if len(username) < 3 or len(username) > 20:
                username_error = "Usernames must be between 3 and 20 characters"
            else:
                if username.isspace():
                    username_error = "Usernames cannot contain spaces"

        #password verification
        if password == password_error:
            password_error = "This field cannot be left blank"
        else:
            if len(password) < 3 or len(password) > 20:
                password_error = "Passwords must be between 3 and 20 character"
            else:
                if password.isspace():
                    password_error = "Password cannot contain spaces"

        if verify == verify_error:
            verify_error = "This field cannot be left blank"
        else:
            if verify != password:
                verify_error = "Passwords don't match. Please try again"

        #Email verification
        if email != "":
            if len(email) < 3 or len(email) > 20:
                email_error = "Email must be between 3 and 20 characters"
            else:
                if "@" not in email:
                    email_error = "Email must include '@' symbol"
                elif "." not in email:
                    email_error = "Email must include a '.'"



        if not username_error and not password_error and not verify_error and not email_error:
            return render_template('welcome.html', name = username)

    # redirect if errors
        return render_template("index.html",
            username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error,
            username=username,
            email=email)

    else:
        return redirect('/')

app.run()
