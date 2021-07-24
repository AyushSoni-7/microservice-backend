from flask_restful import Resource
from data.data import CategoriesData


class Category(Resource):

    def get(self, category_id: int):
        categoryData = next(
            filter(lambda x: x['id'] == category_id, CategoriesData)
            )
        return categoryData, 200

    def delete(self, category_id: int):
        global CategoriesData
        CategoriesData = list(
            filter(lambda x: x['id'] != category_id, CategoriesData)
            )
        return {'message': 'Item deleted'}, 200
