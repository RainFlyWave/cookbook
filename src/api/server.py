from flask import Flask
from flask_restful import Api
from src.views.benefits_views import BenefitsView, ParametrizedBenefitsView
from src.views.ingredient_views import IngredientsView
from src.views.recepie_views import DetailedRecipesView, ParametrizedRecipesView, AllRecepiesView
from src.api.models import db
from src.views.basic_view import BasicView
import os

template_dir = os.path.abspath('src/templates')
static_dir = os.path.abspath('src/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../db/database.db"
api = Api(app)
db.init_app(app)


class Server:
    def __init__(self):
        self.add_api_rules()
        self.add_app_rules()

    def add_api_rules(self):
        api.add_resource(BenefitsView, '/benefits')
        api.add_resource(ParametrizedBenefitsView, '/benefits/<benefit_name>')
        api.add_resource(DetailedRecipesView, '/recepies')
        api.add_resource(ParametrizedRecipesView, '/recepies/<single_recepie>')
        api.add_resource(AllRecepiesView, '/recepies/all')
        api.add_resource(IngredientsView, '/ingredients')

    def add_app_rules(self):
        app.add_url_rule('/', view_func=BasicView.as_view("basic_view"))

    def run(self):
        app.run(debug=True)
