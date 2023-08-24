from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.login_registration_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def main_page():
    return render_template('login.html')

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html', form_data={})

@app.route('/home')
def home():
    return render_template('home.html') #may change html page

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        flash('Registration failed. Please correct the errors below.')
        return render_template('register.html', form_data=request.form)

    password = request.form['password']

    if len(password) < 8:
        flash('Password must be at least 8 characters long')
        return render_template('register.html', form_data=request.form)

    pw_hash = bcrypt.generate_password_hash(password)

    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
    }
    
    user_id = User.create_user(user_data)
    session['user_id'] = user_id
    session['user_name'] = request.form['first_name']

    return redirect('/home')

@app.route('/login', methods=["POST"])
def login():
    user = User.validate_login(request.form)  

    if not user:
        flash('Invalid Email or Password')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect('/')

    session['user_id'] = user.id
    session['user_name'] = user.first_name

    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

