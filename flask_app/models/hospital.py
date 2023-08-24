from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import login_registration_model
from flask_app.models import record
from flask import flash
import pprint


db = "group_proj_schema"

class Hospitals:
    def __init__(self,data):
        self.id = data["id"]
        self.hospital_name = data["hospital_name"]
        self.hospital_address = data["hospital_address"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.Information = []
        
    @classmethod
    def create_hospital(cls,data):
        query = """ INSERT INTO hospitals (hospital_name,hospital_address,user_id)
                VALUES (%(hospital_name)s,%(hospital_address)s,%(user_id)s)
        """
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results)
        
    @classmethod
    def get_all_hospitals(cls):
        query = """ SELECT * FROM hospitals"""
        results = connectToMySQL(db).query_db(query)
        pprint.pprint(results)
        
        hospitals = []
        
        for hospital in results:
            hospitals.append(cls(hospital))
        
        return hospitals
    
    @classmethod
    def update_hospitals(cls,data):
        query = """ UPDATE hospitals SET hospital_name = %(hospital_name)s, hospital_address = %(hospital_address)s
                    WHERE id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results)
        return results
    
    @classmethod
    def delete_hospital(cls,hospital_id):
        query = """ DELETE FROM hospitals
                WHERE id = %(id)s:
            """
        results = connectToMySQL(db).query_db(query,hospital_id)
        pprint.pprint(results)
    
    @classmethod
    def Join_user_hospital(cls,hospital_data):
        query = """ SELECT * FROM users
                JOIN hospitals ON users.id = hospitals.user_id
                WHERE hospitals.id = %(id)s
                """
        results = connectToMySQL(db).query_db(query,hospital_data)
        pprint.pprint(results)
        
        hospitals_user = cls(results[0])
        hospitals_user.Information = results[0]['hospital_name']
        
        return hospitals_user
    