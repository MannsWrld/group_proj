from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.login_registration_model import User
from flask_app.models.hospital import Hospitals


@app.route('/add_hospital')
def host():
    return render_template("add_hospital.html", hospitals=Hospitals.get_all_hospitals())

@app.route('/create/hospital', methods=['POST'])
def create_host():
    data = {
        'hospital_name' : request.form['hospital_name'],
        'hospital_address' : request.form['hospital_address'],
        'user_id' : request.form['user_id']
    }
    Hospitals.create_hospital(data)
    return redirect('/add_hospital')