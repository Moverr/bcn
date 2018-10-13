from flask import Flask,jsonify,render_template,request
from flask_restful import Resource,abort
from model.income import Income,IncomeSchema
from model.expense import Expense,ExpeseSchema
from model.transaction_type import TransactionType


income1 = Income('Salary', 5000);
income2 = Income('Dividends', 200);

transactions = [ 
    income1,
    income2,
  Expense('pizza', 50),
  Expense('Rock Concert', 100)
]


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in transactions:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

class TransactionEntity(Resource):
    def get(self, todo_id):
        # abort_if_todo_doesnt_exist(todo_id)
        schema = IncomeSchema(many=True)
        incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
        )
        
        return  jsonify(incomes.data)

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del transactions[todo_id]
        return '', 204



class TransactionEntityList(Resource):
    def get(self):
        schema = IncomeSchema(many=True)
        incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
        )
        return  jsonify(incomes.data)
    def post(self):
        data = request.get_json();
        income = Income(data['description'],data['amount']);    
        transactions.append(income)
        return self.get()

    

class HelloWord(Resource):
    def get(self):
        return{'Hello':'World!'}

todos = ['Testing Me out','ABCt','BCA']
# todos[0] = 'Testing Me out'
# todos[2] = 'Everything is Possible if you believe'
# todos[3] = 'Come on Let me Trust you with something '



class TodoSimple(Resource):
    def get(self,todo_id=0):
        if(todo_id == 0):
            return todos
       
        return self.getById(todo_id)

    def getById(self, todo_id):
        print("AED")
        return todos[todo_id]

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
