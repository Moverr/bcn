from marshmallow import post_load

from model.transaction import Transaction, TransactionSchema
from model.transaction_type import TransactionType

class Income(Transaction):
    def __init__(self, description, amount):
        super().__init__(description, amount, TransactionType.INCOME)
    
    def __repr__(self):
        return '<Income(name={self.description})>'.format(self=self)


class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self,data):
        return Income(**data)
