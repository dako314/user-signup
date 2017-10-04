from flask import Flask, request, redirect, render_template
import cgi 


app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error=""
    password_error=""
    verify_error=""
    email_error=""

    #username = escape(username, quote=True)
   # password = escape(password, quote=True)
    #verify = escape(verify, quote=True)
   # email = escape(email, quote=True)


    if " " in username or len(username) <3 or len(username) >20: 
        username_error = "Invalid username"
        username = ""
    if password != " " in password or len(password) <3 or len(password) >20:
        password_error = "Invalid password"
        password = ""
    if verify =="" or verify !=password:
        verify_error= "Invalid verification" 
        verify = ''
    if email != "": 
        if "@" not in email or "." not in email or len(email)<3 or len(email)>20:
            email_error = "Invalid email"

    if not email_error and not username_error and not verify_error and not password_error:
        return render_template("welcome.html", username = username)

    else:
        return render_template("index.html" 
                                        , username_error = username_error
                                        , password_error = password_error
                                        , verify_error = verify_error
                                        , email_error = email_error
                                        , username = username
                                        , email = email)




app.run()