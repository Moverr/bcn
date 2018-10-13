from flask import Flask,jsonify,render_template,request
from flask_restful import Resource,Api
from entity.entities import HelloWord,TodoSimple,TransactionEntityList,TransactionEntity
from model.income import Income,IncomeSchema
from model.expense import Expense,ExpeseSchema
from model.transaction_type import TransactionType
 


app = Flask(__name__)
api = Api(app)
income1 = Income('Salary', 5000);
income2 = Income('Dividends', 200);

transactions = [ 
    income1,
    income2,
  Expense('pizza', 50),
  Expense('Rock Concert', 100)
]



incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

 
 
# @app.route('/')
api.add_resource(TransactionEntityList,'/transactions')
api.add_resource(TransactionEntity,'/tr/<todo_id>')
# def hello_world():
#     schema = IncomeSchema(many=True)
#     incomes = schema.dump(
#     filter(lambda t: t.type == TransactionType.INCOME, transactions)
#     )
#     return  jsonify(incomes.data)

# @app.route('/', methods=['POST'])
# def add_income():
  
#    data = request.get_json();
#    income = Income(data['description'],data['amount']);    
#    transactions.append(income)
#    return '',204

#  pdb.set_trace()
# api.add_resource(HelloWord,'/')
# api.add_resource(TodoSimple,  '/todo','/todo/<int:todo_id>')
 

# api.add_resource(TodoSimple,  '/todos/<todo_id>')




if __name__ == '__main__':
    app.run(
        debug=True,
        port=app.config['PORT'] if 'PORT' in app.config else 5000,
        host=app.config['BIND'] if 'BIND' in app.config else '127.0.0.1'
        )