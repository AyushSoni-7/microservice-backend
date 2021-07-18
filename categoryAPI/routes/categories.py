from flask import Blueprint, request, jsonify, json
from data.data import CategoriesData


category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/', methods=["GET"])
def getCategories():
    return {'categories': CategoriesData}, 200


@category_blueprint.route('/<category_id>', methods=["GET"])
def getCategory(category_id):
    retval = [
        data for data in CategoriesData if data['id'] == int(category_id)
        ]
    response = jsonify(retval[0])
    response.status_code = 200
    return response


@category_blueprint.route('/', methods=["POST"])
def addCategory():
    data = request.get_json()
    print(data)
    return jsonify(data), 200


@category_blueprint.route('/', methods=["PUT"])
def updateCategory():
    data = request.get_json()
    for d in CategoriesData:
        if d['id'] == data['id']:
            d.update(data)
            print(d)
    print(CategoriesData)
    return json.dumps(
        {'success': True}), 200, {'ContentType': 'application/json'}


@category_blueprint.route('/<category_id>', methods=["DELETE"])
def deleteCategory(category_id):
    global CategoriesData
    print(len(CategoriesData))
    CategoriesData = [
        d for d in CategoriesData if d.get('id') != int(category_id)
        ]
    print(len(CategoriesData))
    return json.dumps(
        {'success': True}), 200, {'ContentType': 'application/json'}
