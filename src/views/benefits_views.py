from flask_restful import Resource
from flask import jsonify
from src.api.models import BenefitModel
from src.helpers.db_helpers import get_single_benefit, get_all_benefits


class BenefitsView(Resource):
    def get(self):
        return jsonify(get_all_benefits())


class ParametrizedBenefitsView(Resource):
    def get(self, benefit_name):
        return jsonify(get_single_benefit(benefit_name))
