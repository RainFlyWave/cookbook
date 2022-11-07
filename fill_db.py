import sqlite3
from src.api.server import app
from src.api.models import db, RecipeModel, IngredientModel, BenefitModel
import json


with app.app_context():
    db.create_all()

    with open("assets/recipes.txt", "r") as file_handler:
        for i in file_handler:
            a = i.rstrip('\n').lower()
            change_to_commit = RecipeModel(name=a)
            db.session.add(change_to_commit)
        db.session.commit()

    with open("assets/ingredients.txt", "r") as file_handler:
        for i in file_handler:
            a = i.rstrip('\n').lower()
            change_to_commit = IngredientModel(name=a)
            print(change_to_commit)
            db.session.add(change_to_commit)
        db.session.commit()

    with open("assets/benefits.txt", "r") as file_handler:
        for i in file_handler:
            a = i.rstrip('\n').lower()
            change_to_commit = BenefitModel(name=a)
            db.session.add(change_to_commit)
        db.session.commit()

    with open("assets/recipes_all.json", "r") as file:
        a = json.load(file)

    for recepie_obj in a:
        recp_name = recepie_obj.get("recipe_name").lower()
        obj = RecipeModel.query.filter_by(name=recp_name).first()
        for ingredient in recepie_obj.get("ingredients"):
            ingredient = ingredient.lower()
            ingr_obj = IngredientModel.query.filter_by(name=ingredient).first()
            print(ingredient, ingr_obj)
            obj.ingredients.append(ingr_obj)

        for benefit in recepie_obj.get("benefits"):
            benefit = benefit.lower()
            benefit_obj = BenefitModel.query.filter_by(name=benefit).first()
            print(benefit, benefit_obj)
            obj.benefits.append(benefit_obj)
        db.session.commit()
