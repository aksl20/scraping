#-*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, output_json
from scraping import get_game_data
import bdd

class UnicodeApi(Api):
    def __init__(self, *args, **kwargs):
        super(UnicodeApi, self).__init__(*args, **kwargs)
        self.app.config['RESTFUL_JSON'] = {
            'ensure_ascii': False
        }
        self.representations = {
            'application/json; charset=utf-8': output_json
        }

app = Flask(__name__)
api = UnicodeApi(app)

class GameListAPI(Resource):
    def get(self):
        return jsonify({'tasks': bdd.games})

class Nintendo3DSListAPI(Resource):
    def get(self):
        return jsonify({'tasks': bdd.nintendo3DS})

class Nintendo3DSAPI(Resource):
    def get(self, task_id):
        task = [task for task in bdd.nintendo3DS if task['id'] == task_id]
        result = get_game_data(url_website=task[0]['url'], titles_xpath=task[0]['titles_xpath'],\
                              url_xpath=task[0]['url_xpath'], prices_xpath=task[0]['prices_xpath'])
        return result

api.add_resource(GameListAPI, '/rakutenscraping/api/v1.0/games', endpoint = 'games')
api.add_resource(Nintendo3DSListAPI, '/rakutenscraping/api/v1.0/games/3DS', endpoint = '3DS')
api.add_resource(Nintendo3DSAPI, '/rakutenscraping/api/v1.0/games/3DS/<string:task_id>')

if __name__ == '__main__':
        app.run()
