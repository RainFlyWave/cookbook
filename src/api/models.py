from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

ingredients_relation = db.Table(
    'ingredients_relation',
    db.Column('recepie_id', db.Integer, db.ForeignKey('recipe_model.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient_model.id'))
)

benefit_relation = db.Table(
    'benefits_relation',
    db.Column('recepie_id', db.Integer, db.ForeignKey('recipe_model.id')),
    db.Column('benefit_id', db.Integer, db.ForeignKey('benefit_model.id'))
)


class RecipeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    ingredients = db.relationship('IngredientModel', secondary=ingredients_relation, backref='ingredients')
    benefits = db.relationship('BenefitModel', secondary=benefit_relation, backref='benefits')

    def extract_list(self, passed_list: list):
        return_list = []
        for obj in passed_list:
            return_list.append(obj.name.capitalize())
        return return_list

    def serialize_single(self):
        return {
            "id": self.id,
            "name": self.name.capitalize()
        }

    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name.capitalize(),
            "ingredients": self.extract_list(self.ingredients),
            "benefits": self.extract_list(self.benefits)
        }


class IngredientModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def serialize(self):
        return {
            "name": self.name
        }


class BenefitModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    recipes = db.relationship('RecipeModel', secondary=benefit_relation, backref='recipes')

    def extract_list(self, passed_list: list):
        return_list = []
        for obj in passed_list:
            return_list.append(obj.name.capitalize())
        return return_list

    def serialize(self):
        return {
            "name": self.name.capitalize(),
            "recipes": self.extract_list(self.recipes)
        }
