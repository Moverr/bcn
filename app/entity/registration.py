from flask import Flask,jsonify,render_template,request
from flask_restful import Resource,abort
from model.income import Income,IncomeSchema
from model.expense import Expense,ExpeseSchema
from model.transaction_type import TransactionType
from model.registration import Registration as AccountRegistration

 

registrations = [
    registration
]


class List(Resource):
    def get(self):
        schema = IncomeSchema(many=True)
        incomes = schema.dump(
        filter(registrations)
        )
        return  jsonify(incomes.data)
    def post(self):
        data = request.get_json();
        registration = AccountRegistration('username', "password","email");
        registrations.append(registration)
        return self.get()


