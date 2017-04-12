#-*- coding: utf-8 -*-

from scraping import bdd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, output_json
from scraping.lib import get_game

class UnicodeApi(Api):
    def __init__(self, *args, **kwargs):
        super(UnicodeApi, self).__init__(*args, **kwargs)
        self.app.config['RESTFUL_JSON'] = {
            'ensure_ascii': False
        }
        self.representations = {
            'application/json; charset=utf-8': output_json
        }

# First selection level
class GameListAPI(Resource):
    def get(self):
        return jsonify(bdd.games)

class SoftwareListAPI(Resource):
    def get(self):
        return jsonify(bdd.softwares)

# Second selection level
class Nintendo3DSListAPI(Resource):
    def get(self):
        return jsonify(bdd.nintendo3DS)

class Playstation4ListAPI(Resource):
    def get(self):
        return jsonify(bdd.playstation4)

class KeyboardMouseListAPI(Resource):
    def get(self):
        return jsonify(bdd.keyboardMouse)

class PCComponentListAPI(Resource):
    def get(self):
        return jsonify(bdd.pccomponent)

# Selection the web page to scrap
class Playstation4API(Resource):
    def get(self, data_id):
        result = get_game(bdd=bdd.playstation4, data_id=data_id)
        return result

class Nintendo3DSAPI(Resource):
    def get(self, data_id):
        result = get_game(bdd=bdd.nintendo3DS, data_id=data_id)
        return result

class KeyboardMouseAPI(Resource):
    def get(self, data_id):
        result = get_game(bdd=bdd.keyboardMouse, data_id=data_id)
        return result

class PCComponentAPI(Resource):
    def get(self, data_id):
        result = get_game(bdd=bdd.pccomponent, data_id=data_id)
        return result

def main():
    app = Flask(__name__)
    api = UnicodeApi(app)

    api.add_resource(SoftwareListAPI, '/rakutenscraping/api/v1.0/software')

    api.add_resource(KeyboardMouseListAPI, '/rakutenscraping/api/v1.0/software/keyboardmouse')
    api.add_resource(KeyboardMouseAPI, '/rakutenscraping/api/v1.0/software/keyboardmouse/<string:data_id>')
    api.add_resource(PCComponentListAPI, '/rakutenscraping/api/v1.0/software/pccomponent')
    api.add_resource(PCComponentAPI, '/rakutenscraping/api/v1.0/software/pccomponent/<string:data_id>')

    api.add_resource(GameListAPI, '/rakutenscraping/api/v1.0/games')

    api.add_resource(Nintendo3DSListAPI, '/rakutenscraping/api/v1.0/games/3DS')
    api.add_resource(Nintendo3DSAPI, '/rakutenscraping/api/v1.0/games/3DS/<string:data_id>')
    api.add_resource(Playstation4ListAPI, '/rakutenscraping/api/v1.0/games/PS4')
    api.add_resource(Playstation4API, '/rakutenscraping/api/v1.0/games/PS4/<string:data_id>')
    
    app.run()

if __name__ == '__main__':
    main()
