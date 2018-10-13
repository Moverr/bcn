import datetime as dt 

from flask_marshmallow import Schema, fields

class Registration():
    def __init__(self,username,passowrd,email):
        self.username = username
        self.password = passowrd
        self.date_created = dt.datetime.now()
    
def __repr__(self):
    return '<Registration(name={self.username})>'.format(self=self)


class RegistrationSchema(Schema):
    pass;