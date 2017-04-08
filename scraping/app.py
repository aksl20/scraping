#-*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

e = create_engine('sqlite:///rakuten.db')

app = Flask(__name__)
api = Api(app)

games = [
    {
        'id': 1,
        'title': u'Nintendo 3DS',
        'description': u'A lot of Nitendo 3DS games from rakuten.co.jp', 
        'done': False
    }
]
class GameListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
            help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListAPI, self).__init__()

    def get(self):
        pass

@app.route('/rakutenscraping/api/v1.0/games', methods=['GET'], endpoint = '/')
def get_tasks():
    return jsonify({'tasks':games})

api.add_resource(GameListAPI, '/rakutenscraping/api/v1.0/games', endpoint = 'games')

if __name__ == '__main__':
     app.run()
