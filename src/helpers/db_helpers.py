from src.api.models import RecipeModel, BenefitModel


def get_single_recepie(passed_name: str):
    single_object = RecipeModel.query.filter_by(name=passed_name.lower()).first()
    return single_object.serialize_all()


def get_all_detailed_recepies():
    all_recepies = []
    recepies = RecipeModel.query.all()
    for recepie in recepies:
        all_recepies.append(recepie.serialize_all())
    return all_recepies


def get_all_recepies():
    all_recepies = []
    recepies = RecipeModel.query.all()
    for recepie in recepies:
        all_recepies.append(recepie.serialize_single())
    return all_recepies


def get_single_benefit(passed_name: str):
    single_object = BenefitModel.query.filter_by(name=passed_name.lower()).first()
    return single_object.serialize()


def get_all_benefits():
    all_benefits = []
    benefits = BenefitModel.query.all()
    for benefit in benefits:
        all_benefits.append(benefit.serialize())
    return all_benefits
