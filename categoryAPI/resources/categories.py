from flask_restful import Resource
from flask import request
from data.data import CategoriesData


class Categories(Resource):

    def get(self):
        data = CategoriesData
        return {'categories': data}, 200

    def post(self):
        data = request.get_json()
        return data, 200

    def put(self):
        data = request.get_json()
        categoryData = next(
            filter(lambda x: x['id'] == data['id'], CategoriesData)
            )
        categoryData.update(data)
        return categoryData, 200
