#-*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, output_json
from scraping import get_game_data
from json import dumps

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


games = [
    {
        'id': u'3DS',
        'title': u'Nintendo 3DS',
        'description': u'A lot of product in relation with Nitendo 3DS from rakuten.co.jp', 
        'done': False
    }
]

nintendo3DS = [
    {
        'id': u'device',
        'description': u'You want to by a 3DS, this is the right place', 
        'url': 'http://books.rakuten.co.jp/search/dt/g006508001/',
        'titles_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span",
        'url_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href",
        'prices_xpath': "//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em",
        'done': False
    },
    {
        'id': u'component',
        'description': u'Here you can find additional component for nintendo 3DS',
        'url': 'http://books.rakuten.co.jp/search/dt?mt=0&o=0&cy=0&h=30&g=006508002&e=0&v=2&spv=2&s=1&sv=30',
        'titles_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span",
        'url_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href",
        'prices_xpath': "//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em",
        'done': False
    }
]

class GameListAPI(Resource):
    def get(self):
        return jsonify({'tasks': games})

class Nintendo3DSListAPI(Resource):
    def get(self):
        return jsonify({'tasks': nintendo3DS})

class Nintendo3DSAPI(Resource):
    def get(self, task_id):
        task = [task for task in nintendo3DS if task['id'] == task_id]
        result = get_game_data(url_website=task[0]['url'], titles_xpath=task[0]['titles_xpath'],\
                              url_xpath=task[0]['url_xpath'], prices_xpath=task[0]['prices_xpath'])
        return result

api.add_resource(GameListAPI, '/rakutenscraping/api/v1.0/games', endpoint = 'games')
api.add_resource(Nintendo3DSListAPI, '/rakutenscraping/api/v1.0/games/3DS', endpoint = '3DS')
api.add_resource(Nintendo3DSAPI, '/rakutenscraping/api/v1.0/games/3DS/<string:task_id>')

if __name__ == '__main__':
        app.run()
