#-*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:///rakuten.db')

app = Flask(__name__)
api = Api(app)

class PSP(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from PSP")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} 
        return result

api.add_resource(PSP, '/psp')

if __name__ == '__main__':
     app.run()
