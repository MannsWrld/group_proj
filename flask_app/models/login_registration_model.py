from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

Email_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
password_REGEX = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,15}$")

db = 'group_proj_schema'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = 'SELECT * FROM users;'
        db_response = connectToMySQL(db).query_db(query)
        users = []
        for user in db_response:
            new_user =cls(user)
            users.append(new_user)
        return users
    
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        db_response = connectToMySQL(db).query_db(query, data)
        return db_response
    
    @staticmethod
    def validate_user(data):
        print('data', data)
        is_valid = True
        if len(data['first_name']) < 1:
            flash('First name must be more than one character')
            print('first name not good')
            is_valid = False
        if not Email_REGEX.match(data['email']):
            flash('Invalid Email and/or Password')
            print('email no good')
            is_valid = False
        if not re.search(password_REGEX, data['password']):
            flash('Password does not meet requirements')
            print('Password no good')
            is_valid = False
        print('validations complete')
        return is_valid
    
    @classmethod
    def find_user(cls, user_email):
        email_dict ={
            'email': user_email 
        }
        print('email_dict', email_dict)
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        db_response = connectToMySQL(db).query_db(query, email_dict)
        print('db_response', db_response)
        if db_response:
            return True
        return cls(db_response[0])

    @classmethod
    def validate_login(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(db).query_db(query, data)
        return results
