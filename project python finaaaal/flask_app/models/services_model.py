from projet_python.config.mysqlconnection import connectToMySQL
from projet_python import DB_NAME
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Service:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod 
    def CreateService(self,data):
        query=  """
                INSERT INTO services (title , description) 
                VALUES (%(title)s,%(description)s);
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    
    @classmethod
    def UpdateService(self,data):
        query = """ 
                UPDATE services SET
                title=%(title)s,description=%(description)s
                WHERE id=%(id)s;
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    
    @classmethod
    def ListService(self):
        query = """
                SELECT * FROM services;
                """
        results =  connectToMySQL(DB_NAME).query_db(query)
        all_rec=[]
        for row in results:
            all_rec.append(cls(row))
        return all_rec
    
    @classmethod
    def delete_service(cls,data):
        query = """
                DELETE FROM services WHERE id=%(id)s
                """
        return  connectToMySQL(DB_NAME).query_db(query,data)