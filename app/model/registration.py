import datetime as dt 
from marshmallow import Schema,fields
from marshmallow import post_load

class Registration():
    def __init__(self,username,passowrd,email):
        self.username = username
        self.password = passowrd
        self.email = email
        self.date_created = dt.datetime.now()
    
def __repr__(self):
    return '<Registration(name={self.username})>'.format(self=self)


class RegistrationSchema(Schema):
    username = fields.Str()
    # password = fields.Str()
    email = fields.Str()
    date_created = fields.Date() 
    @post_load
    def make_registration(self,data):
        return Registration(**data)