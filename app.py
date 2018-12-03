from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

TASKS = {'task1':{'task':'blah'}, 'task2':{'task':'blah1'}}

def abort_if_task_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(404, message="Task {} doesn't exist".format(task_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class TaskList(Resource):
    def get(self):
        return TASKS

class Task(Resource):
    def get(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        return TASKS[task_id]

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(TaskList, '/tasklist')
api.add_resource(Task, '/task/<task_id>')

if __name__ == '__main__':
    app.run()