from flask import request
from flask_restful import Resource

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
