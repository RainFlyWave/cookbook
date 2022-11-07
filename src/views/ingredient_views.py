from flask_restful import Resource
from flask import jsonify
from src.api.models import IngredientModel


class IngredientsView(Resource):
    def get(self):
        return '', 200
