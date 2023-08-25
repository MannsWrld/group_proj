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

@app.route('/delete_records', methods=['POST'])
def delete_records():
    record_id = request.form.get('record_id')
    print('record--id', record_id)
    Records.delete_record(record_id)
    return redirect('/login_page')

@app.route('/edit_records/<user_id>', methods=['POST'])
def edit_records(user_id):
    user = User.get_user_by_id(user_id)
    record = Records.get_record_by_user_id(user_id)
    return render_template('edit_record.html', user=user, record = record)

@app.route('/save_record', methods=['POST'])
def save_record():
    user_id = request.form.get('user_id')
    record = request.form['record']
    Records.update_record(user_id, record)
    return redirect('/home')
