from marshmallow import post_load

from model.transaction import Transaction, TransactionSchema
from model.transaction_type import TransactionType

class Expense(Transaction):
    def __init__(self, description, amount):
        super().__init__(description, amount, TransactionType.EXPENSE)
    
    def __repr__(self):
        return '<Income(name={self.description})>'.format(self=self)


class ExpeseSchema(TransactionSchema):
    @post_load
    def make_income(self,data):
        return Expense(**data)
