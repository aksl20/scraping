#-*- coding: utf-8 -*-

import bdd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, output_json
from scraping import get_game

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
        return jsonify(bdd.games)

class Nintendo3DSListAPI(Resource):
    def get(self):
        return jsonify(bdd.nintendo3DS)

class Playstation4ListAPI(Resource):
    def get(self):
        return jsonify(bdd.playstation4)

class Playstation4API(Resource):
    def get(self, data_id):
        result = get_game(bdd=bdd.playstation4, data_id=data_id)
        return result

class Nintendo3DSAPI(Resource):
    def get(self, data_id):
        result = get_game(bdd=bdd.nintendo3DS, data_id=data_id)
        return result

api.add_resource(GameListAPI, '/rakutenscraping/api/v1.0/games')
api.add_resource(Nintendo3DSListAPI, '/rakutenscraping/api/v1.0/games/3DS')
api.add_resource(Nintendo3DSAPI, '/rakutenscraping/api/v1.0/games/3DS/<string:data_id>')
api.add_resource(Playstation4ListAPI, '/rakutenscraping/api/v1.0/games/PS4')
api.add_resource(Playstation4API, '/rakutenscraping/api/v1.0/games/PS4/<string:data_id>')


if __name__ == '__main__':
    app.run()
