from projet_python.config.mysqlconnection import connectToMySQL
from projet_python import DB_NAME
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class booking:
    def __init__(self,data):
        self.id=data['id']
        self.service_id=data['service_id']
        self.user_id=data['user_id']
        self.cleaner_id=data['cleaner_id']
        self.date_cleaning=data['date_cleaning']
        self.status=data['status']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    #########create booking########################
    def create_booking(self,data):
        query=  """
                INSERT INTO bookings (service_id,user_id,cleaner_id,date_cleaning,status) 
                VALUES (%(service_id)s,%(user_id)s,%(cleaner_id)s,%(date_cleaning)s,%(status)s);
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result      
    ################update booking##########                         
    def Update_booking(self,data):
        query = """ 
                UPDATE bookings SET
                service_id=%(service_id)s,cleaner_id=%(cleaner_id)s,date_cleaning=%(date_cleaning)s,
                status=%(status)s
                WHERE id=%(id)s;
                """
        result=connectToMySQL(DB_NAME).query_db(query,data)
        return result
    ############get all booking########
    def get_all_bookings(self,data):
        query = """ 
                SELECT * FROM bookings WHERE 
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    ############get booking by id########
    def get_booking_by_id(self,data):
        query = """ 
                SELECT * FROM bookings WHERE id =%(id)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    ############ bookings by user##############
    def get_bookings_by_user(self,data):
        query = """ 
                SELECT * FROM bookings WHERE user_id =%(user_id)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    ########### bookings by cleaner##########
    def get_bookings_by_cleaner(self,data):
        query = """ 
                SELECT * FROM bookings WHERE cleaner_id =%(cleaner_id)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    ########### bookings by service#########
    def get_bookings_by_service(self,data):
        query = """ 
                SELECT * FROM bookings WHERE service_id =%(service_id)s
                """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        if (result):
            return cls(result[0])
        return False
    ########## delete booking##########
    @classmethod
    def remove_booking(cls,data):
        query="""DELETE FROM bookings WHERE id=%(id)s
        """
        return  connectToMySQL(DATABASE).query_db(query,data)
    