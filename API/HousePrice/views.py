__VERSION__ = "0.0.1"

try:
    import  os
    import sys
    import json
    from flask import request

    from flask import jsonify, make_response
    from flask import Flask

    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse

    print("All modules are loaded ")
except Exception as e:
    print("Error : {} ".format(e))


app = Flask(__name__)
api = Api(app)


class Processor(object):

    def __init__(self, data = {}):
        self.__price = 0.0
        self.data = data

    def get(self):
        try:
            self.__price += 75.0  *  self.data.get('GrLivArea', '0.0')
            self.__price += 54.0  *  self.data.get('TotalBsmtSF', '0.0')
            self.__price += 51.0  *  self.data.get('GarageArea', '0.0')
            self.__price += 671.0 *  self.data.get('YearBuilt', '0.0')
            return self.__price
        except Exception as e:
            print('error : {} '.format(e))
            return -1.0


class Controller(Resource):

    def __init__(self):
        self.GrLivArea = parser.parse_args().get('GrLivArea', None)
        self.TotalBsmtSF = parser.parse_args().get('TotalBsmtSF', None)
        self.GarageArea = parser.parse_args().get('GarageArea', None)
        self.YearBuilt = parser.parse_args().get('YearBuilt', None)
        self.__data = {
            "GrLivArea":self.GrLivArea,
            "TotalBsmtSF":self.TotalBsmtSF,
            "GarageArea":self.GarageArea,
            "YearBuilt":self.YearBuilt
        }

    def get(self):
        try:
            _instance  = Processor(data=self.__data)
            res = _instance.get()
            return res,200
        except Exception as e:
            return "Error : {} ".format(e), 400


parser = reqparse.RequestParser()
parser.add_argument("GrLivArea", type=float, required=True, help="GrLivArea is required  [float]")
parser.add_argument("TotalBsmtSF", type=float, required=True, help="GrLivArea is required  [float]")
parser.add_argument("GarageArea", type=float, required=True, help="GrLivArea is required  [float]")
parser.add_argument("YearBuilt", type=float, required=True, help="GrLivArea is required  [float]")


