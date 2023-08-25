from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import login_registration_model
import pprint
from flask_app import app
from flask import flash

db = "group_proj_schema"

class Records:
    def __init__(self,data):
        self.id = data["id"],
        self.name = data["name"],
        self.record = data["record"],
        self.email = data["email"],
        self.user_id = data["user_id"],
        self.created_at = data["created_at"],
        self.updated_at = data["updated_at"],
        self.patient = []
    
    @classmethod
    def create_record(cls,data):
        query = """ INSERT INTO records (name,record,email,user_id)
                VALUES (%(name)s,%(record)s,%(email)s,%(user_id)s)
        """
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results)
        
    @classmethod
    def get_all_records(cls):
        query = """ SELECT * FROM records"""
        results = connectToMySQL(db).query_db(query)
        pprint.pprint(results)
        
        records = []
        
        for record in results:
            records.append(cls(record))
            
        return records
    
    @classmethod
    def update_records(cls,data):
        query = """ UPDATE records SET name = %(name)s,email = %(email)s,record = %(record)s
                    WHERE id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results)
        return results
    
    @classmethod
    def delete_records(cls, record_id):
        query = """ DELETE FROM records
                WHERE id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query,record_id)
        pprint.pprint(results)
        return results
    
    @classmethod
    def get_one_record(cls,data):
        query = """SELECT * FROM records
                WHERE id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])
    
    @staticmethod
    def validate_record_info(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            flash("Must put full first name")
            is_valid = False
        if len(form_data['allergies']) < 3:
            flash("Allergies was inccorect")
            is_valid = False
        if len(form_data[medical]) < 3:
            flash("medical Info is incorrecr")
            is_valid = False
        if len(form_data[sickness]) < 3:
            flash("Sickness must be filled in")
            is_valid = False
        return is_valid