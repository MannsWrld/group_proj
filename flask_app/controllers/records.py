from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.login_registration_model import User
from flask_app.models.record import Records

@app.route('/new/information')
def user_info():
    return render_template("add_record.html")

@app.route('/submit/user_info',methods=["POST"])
def submit_info():
    data = {
        'name' : request.form['name'],
        'record' : request.form['record'],
        'email' : request.form['email'],
        'user_id' : request.form['user_id']
    }
    Records.create_record(data)
    return redirect('/home')

@app.route('/delete_records')
def delete_records():
    Records.delete_records
    return redirect('/login_page')