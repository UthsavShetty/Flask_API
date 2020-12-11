__VERSION__ = "0.0.1"

try:
    import  os
    import sys

    sys.path.append(os.getcwd())
    sys.path.append("house_coordinates.csv")

    import json
    from flask import request

    from flask import jsonify, make_response
    from flask import Flask

    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse

    import numpy as np
    import math

    import pandas as pd
    import threading

    print("All modules are loaded ")
except Exception as e:
    print("Error : {} ".format(e))


app = Flask(__name__)
api = Api(app)

class HouseLookupController(Resource):

    def __init__(self):

        self.x1 = parser.parse_args().get('x1', None)
        self.x2 = parser.parse_args().get('x2', None)
        self.x3 = parser.parse_args().get('x3', None)
        self.x4 = parser.parse_args().get('x4', None)
        self.x5 = parser.parse_args().get('x5', None)
        self.x6 = parser.parse_args().get('x6', None)
        self.x7 = parser.parse_args().get('x7', None)

        self.y1 = parser.parse_args().get('y1', None)
        self.y2 = parser.parse_args().get('y2', None)
        self.y3 = parser.parse_args().get('y3', None)
        self.y4 = parser.parse_args().get('y4', None)
        self.y5 = parser.parse_args().get('y5', None)
        self.y6 = parser.parse_args().get('y6', None)
        self.y7 = parser.parse_args().get('y7', None)

    def get(self):
        try:
            # [(x,y) ...... ]
            data = DataTransform.get(arr2=[self.x1,
                                           self.y1,
                                           self.x2,
                                           self.y2,
                                           self.x3,
                                           self.y3,
                                           self.x4,
                                           self.y4,
                                           self.x5,
                                           self.y5,
                                           self.x6,
                                           self.y6,
                                           self.x7,
                                           self.y7])

            # [(x,y) .....]
            # [[x,y],  [x1,y1], ......]
            _ = [[x, y] for x, y in data ]

            AREA1 = Polygon.area(vertices=_)     # Calculate Area for the Polygon


            df = pd.read_csv("house_coordinates.csv")
            df1 = df.to_dict('record')

            Result = []

            for x in df1:

                x1 = x.get("x1")
                x2 = x.get("x2")
                x3 = x.get("x3")
                x4 = x.get("x4")

                y1 = x.get("y1")
                y2 = x.get("y2")
                y3 = x.get("y3")
                y4 = x.get("y4")


                # processor class with convert the data in [(x,y), .....]
                # Area cal karaga and then
                AREA2  = Processor.get([x1, y1, x2, y2, x3, y3, x4, y4])

                if AREA2 < AREA1:
                    Result.append(x)
                else:
                    pass

            return Result

        except Exception as e:
            return "Error : {} ".format(e)



class Processor(object):

    @staticmethod
    def get(arr1):
        X = []
        Y = []

        for i in range(0, len(arr1)):

            evenIndex = i * 2
            oddIndex = 2  * i + 1

            if  evenIndex < len(arr1):
                X.append(arr1[evenIndex])

            if oddIndex < len(arr1):
                Y.append(arr1[oddIndex])

        data = list(zip(X,Y))

        coords = data

        # get x and y in vectors
        x = [point[0] for point in coords]
        y = [point[1] for point in coords]
        # shift coordinates
        x_ = x - np.mean(x)
        y_ = y - np.mean(y)

        # calculate area

        correction = x_[-1] * y_[0] - y_[-1] * x_[0]

        main_area = np.dot(x_[:-1], y_[1:]) - np.dot(y_[:-1], x_[1:])

        return 0.5 * np.abs(main_area + correction)


class DataTransform(object):

    @staticmethod
    def get(arr2):

        X = []
        Y = []
        """
        [
            (x,y),
            (x1,y1)
        ]
        """
        for i in range(0, len(arr2)):

            evenIndex = i * 2
            oddIndex = 2  * i + 1

            if  evenIndex < len(arr2):
                X.append(arr2[evenIndex])

            if oddIndex < len(arr2):
                Y.append(arr2[oddIndex])

        data2 = list(zip(X,Y))
        return data2


class Polygon(object):

    @staticmethod
    def area(vertices):

        #A function to apply the Shoelace algorithm
        numberOfVertices = len(vertices)

        sum1 = 0
        sum2 = 0

        for i in range(0,numberOfVertices-1):
            sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
            sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]

        #Add xn.y1
        sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]
        #Add x1.yn
        sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]

        area = abs(sum1 - sum2) / 2
        return area




parser = reqparse.RequestParser()

parser.add_argument("x1", type=float, required=True, help=" x1 [float]")
parser.add_argument("x2", type=float, required=True, help=" x2 [float]")
parser.add_argument("x3", type=float, required=True, help=" x3 [float]")
parser.add_argument("x4", type=float, required=True, help=" x4 [float]")
parser.add_argument("x5", type=float, required=True, help=" x5 [float]")
parser.add_argument("x6", type=float, required=True, help=" x6 [float]")
parser.add_argument("x7", type=float, required=True, help=" x7 [float]")


parser.add_argument("y1", type=float, required=True, help=" y1 [float]")
parser.add_argument("y2", type=float, required=True, help=" y2 [float]")
parser.add_argument("y3", type=float, required=True, help=" y3 [float]")
parser.add_argument("y4", type=float, required=True, help=" y4 [float]")
parser.add_argument("y5", type=float, required=True, help=" y5 [float]")
parser.add_argument("y6", type=float, required=True, help=" y6 [float]")
parser.add_argument("y7", type=float, required=True, help=" y7 [float]")



