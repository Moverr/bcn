from flask import Flask,jsonify,render_template,request
from flask_restful import Resource,abort
from model.income import Income,IncomeSchema
from model.registration import  Registration,RegistrationSchema
from model.expense import Expense,ExpeseSchema
from model.transaction_type import TransactionType
from model.registration import Registration as AccountRegistration

 

# //todo: list data 
# registration = AccountRegistration('mooio','password','email');   
# registration2 = AccountRegistration('mooio','password','email');   
# registration3 = AccountRegistration('mooio','password','email');   

registrations = []


class RList(Resource):
    def get(self):
        schema = RegistrationSchema(many=True)       
        registrationList = schema.dump( 
        filter(lambda t: len(t.username) > 0 , registrations)
        )
        return  jsonify(registrationList.data)
    def post(self):
        data = request.get_json(); 
        registration = AccountRegistration(data['username'],data['password'],data['email']);   
        registrations.append(registration)
        return self.get()


