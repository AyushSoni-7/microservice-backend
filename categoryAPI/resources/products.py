from flask_restful import Resource
from models.product_category_map import ProductCategoryMap


class Products(Resource):
    def get(self, category_id: int):
        return {
          'products': ProductCategoryMap.get_products(category_id)
          }, 200
