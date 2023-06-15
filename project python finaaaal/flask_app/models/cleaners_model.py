from projet_python.config.mysqlconnection import connectToMySQL
from projet_python import DB_NAME
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Cleaner:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data['email']
        self.availability = data['availability']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod 
    def CreateCleaner(self,data):
        query=  """
                INSERT INTO cleaners (first_name , last_name , phone_number , email , availability) 
                VALUES (%(first_name)s,%(last_name)s,%(phone_number)s,%(email)s,%(availability)s);
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    
    @classmethod
    def UpdateCleaner(self,data):
        query = """ 
                UPDATE cleaners SET
                first_name=%(first_name)s,last_name=%(last_name)s,phone_number=%(phone_number)s,
                email=%(email)s,availability=%(availability)s
                WHERE id=%(id)s;
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    
    @classmethod
    def ListCleaner(self):
        query = """
                SELECT * FROM cleaners;
                """
        results =  connectToMySQL(DB_NAME).query_db(query)
        all_rec=[]
        for row in results:
            all_rec.append(cls(row))
        return all_rec
    
    @classmethod
    def get_cleaner_by_availability(cls,data):
        query = """
                SELECT * FROM cleaners WHERE 
                availability=%(availability)s;
                """
        results =  connectToMySQL(DB_NAME).query_db(query)
        all_rec=[]
        for row in results:
            all_rec.append(cls(row))
        return all_rec
    
    @classmethod
    def get_cleaner_by_email(cls,data):
        query=""" SELECT * FROM cleaners WHERE email =%(email)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    
    @classmethod
    def delete_cleaner(cls,data):
        query = """
                DELETE FROM cleaners WHERE id=%(id)s
                """
        return  connectToMySQL(DB_NAME).query_db(query,data)
    
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['first_name'])<2:
            flash("Invalid first name!")
            is_valid=False
        if len(data['last_name'])<2:
            flash("Invalid last name!")
            is_valid=False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email !")
            is_valid=False
        elif Cleaner.get_cleaner_by_email({'email':data['email']}) :
            flash(" already used email adress!")
            is_valid=False
        elif data['availability'] not in ['available','not available'] :
            flash("Select an availability !")
            is_valid=False

        return is_valid
    
    
    
    
    