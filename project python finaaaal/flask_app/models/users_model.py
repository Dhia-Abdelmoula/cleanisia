from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB_NAME
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.if_admin = data['if_admin']
        
        
    @classmethod 
    def create_user(self,data):
        query=  """
                INSERT INTO users (first_name,last_name,email,password) 
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result

    @classmethod
    def update_user(self,data):
        query = """ 
                UPDATE users SET
                first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s
                WHERE id=%(id)s;
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    
    @classmethod
    def change_password(self,data):
        query = """
                UPDATE users SET
                password=%(password)s WHERE
                id=%(id)s;
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result

    @classmethod
    def list_users(self):
        query = """
                SELECT * FROM users;
                """
        results =  connectToMySQL(DB_NAME).query_db(query)
        all_rec=[]
        for row in results:
            all_rec.append(cls(row))
        return all_rec
    
    
    @classmethod
    def get_user_by_email(cls,data):
        query=""" SELECT * FROM users WHERE email =%(email)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    
    @classmethod
    def get_user_by_id(cls,data):
        query=""" SELECT * FROM users WHERE id =%(id)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['first_name'])<2:
            flash("Invalid first name!" , "reg")
            is_valid=False
        elif len(data['last_name'])<2:
            flash("Invalid last name!" , "reg")
            is_valid=False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email !", "reg")
            is_valid=False
        elif User.get_user_by_email({'email':data['email']}) :
            flash(" already used email adress!" , "reg")
            is_valid=False
        elif len(data['password'])<6 :
            flash("Invalid password!" , "reg")
            is_valid=False
        elif data['password'] != data['password_confirm']: 
            flash(" password must  match!" , "reg")
            is_valid=False

        return is_valid
    