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

    def post(self):
        args = parser.parse_args()
        task_id = int(max(TASKS.keys()).lstrip('task')) + 1
        task_id = 'task%i' % task_id
        TASKS[task_id] = {'task': args['task']}
        return TASKS[task_id], 201

class Task(Resource):
    def get(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        return TASKS[task_id]



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<task_id>')

if __name__ == '__main__':
    app.run()