from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

TASKS = {'task1':{'task':'blah'}, 'task2':{'task':'blah1'}}

class TaskList(Resource):
    def get(self):
        return TASKS

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(TaskList, '/tasklist')

if __name__ == '__main__':
    app.run()