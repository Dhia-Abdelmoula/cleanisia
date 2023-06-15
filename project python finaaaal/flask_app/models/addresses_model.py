from projet_python.config.mysqlconnection import connectToMySQL
from projet_python import DB_NAME
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class address:
    def __init__(self,data):
        self.id = data['id']
        self.adr1 = data['adr1']
        self.city = data['city']
        self.state = data['state']
        self.country = data['country']
        self.postal_code = data['postal_code']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def CreateAdress(self,data):
        query=  """
                INSERT INTO addresses (adr1,city,state,country,postal_code) 
                VALUES (%(adr1)s,%(city)s,%(state)s,%(country)s,%(postal_code)s);
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    
    def UpdateAddress(self,data):
        query = """ 
                UPDATE addresses SET
                adr1=%(adr1)s,city=%(city)s,state=%(state)s,
                country=%(country)s,postal_code=%(postal_code)s
                WHERE id=%(id)s;
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    
    def get_address_by_id(cls,data):
        query = """ 
                SELECT * FROM addresses WHERE id =%(id)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    
    
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['adr1'])<2:
            flash("Invalid Address!" , "adr1_error")
            is_valid=False
        if len(data['city'])<2:
            flash("Invalid city!" , "city_error")
            is_valid=False
        if len(data['state'])<2 :
            flash("Invalid state!" , "state_error")
            is_valid=False
        if len(data['state'])<2 :
            flash("Invalid state!" , "state_error")
            is_valid=False
        if len(data['country'])<2 :
            flash("Invalid country!" , "country_error")
            is_valid=False
        if len(data['postal_code'])<2 :
            flash("Invalid postal_code!" , "postal_code_error")
            is_valid=False