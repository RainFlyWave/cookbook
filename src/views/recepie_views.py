from flask_restful import Resource
from flask import jsonify
from src.helpers.db_helpers import get_all_detailed_recepies, get_single_recepie, get_all_recepies


class DetailedRecipesView(Resource):
    def get(self):
        return jsonify(get_all_detailed_recepies())


class ParametrizedRecipesView(Resource):
    def get(self, single_recepie):
        return jsonify(get_single_recepie(single_recepie))


class AllRecepiesView(Resource):
    def get(self, single_ingredient: str):
        return jsonify(get_all_recepies(single_ingredient))
