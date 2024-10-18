from flask import Flask, jsonify
from flask_cors import CORS
import json
import random
import os
import sys

app = Flask(__name__)
cors = CORS(app, origin="*")

with open('/Users/anatole/PhpstormProjects/foodplaner/public/json_food/repas_rouge.json', 'r') as repas_rouge_json:
    repas_rouge = json.load(repas_rouge_json)

with open('/Users/anatole/PhpstormProjects/foodplaner/public/json_food/repas_jaune.json', 'r') as repas_jaune_json:
    repas_jaune = json.load(repas_jaune_json)

with open('/Users/anatole/PhpstormProjects/foodplaner/public/json_food/repas_orange.json', 'r') as repas_orange_json:
    repas_orange = json.load(repas_orange_json)

with open('/Users/anatole/PhpstormProjects/foodplaner/public/json_food/repas_vert.json', 'r') as repas_vert_json:
    repas_vert = json.load(repas_vert_json)

with open('/Users/anatole/PhpstormProjects/foodplaner/public/json_food/sauces.json', 'r') as sauces_json:
    sauces = json.load(sauces_json)

@app.route('/restart')
def restart_script():
    os.execv(sys.executable, ['python'] + sys.argv)

def r_rouge(jour):
    rp_rouge_noms = random.choice(repas_rouge)
    repas_rouge_moment = rp_rouge_noms["moment_plat"]

    if dail_choice_day[jour] == "repas_rouge":
        if repas_rouge_moment["midi"] == 1:
            return rp_rouge_noms["nom"]
        else:
            while repas_rouge_moment["midi"] == 0:
                rp_rouge_noms = random.choice(repas_rouge)
                repas_rouge_moment = rp_rouge_noms["moment_plat"]
                if repas_rouge_moment["midi"] == 1:
                    return rp_rouge_noms["nom"]

    elif dail_choice_night[jour] == "repas_rouge":
        if repas_rouge_moment["soir"] == 1:
            return rp_rouge_noms["nom"]
        else:
            while repas_rouge_moment["soir"] == 0:
                rp_rouge_noms = random.choice(repas_rouge)
                repas_rouge_moment = rp_rouge_noms["moment_plat"]
                if repas_rouge_moment["soir"] == 1:
                    return rp_rouge_noms["nom"]

def r_jaune(jour):
    rp_jaune_noms = random.choice(repas_jaune)
    repas_jaune_moment = rp_jaune_noms["moment_plat"]

    if dail_choice_day[jour] == "repas_jaune":
        if repas_jaune_moment["midi"] == 1:
            return rp_jaune_noms["nom"]
        else:
            while repas_jaune_moment["midi"] == 0:
                rp_jaune_noms = random.choice(repas_jaune)
                repas_jaune_moment = rp_jaune_noms["moment_plat"]
                if repas_jaune_moment["midi"] == 1:
                    return rp_jaune_noms["nom"]

    elif dail_choice_night[jour] == "repas_jaune":
        if repas_jaune_moment["soir"] == 1:
            return rp_jaune_noms["nom"]
        else:
            while repas_jaune_moment["soir"] == 0:
                rp_jaune_noms = random.choice(repas_jaune)
                repas_jaune_moment = rp_jaune_noms["moment_plat"]
                if repas_jaune_moment["soir"] == 1:
                    return rp_jaune_noms["nom"]

def r_orange(jour):
    rp_orange_noms = random.choice(repas_orange)
    repas_orange_moment = rp_orange_noms["moment_plat"]

    if dail_choice_day[jour] == "repas_orange":
        if repas_orange_moment["midi"] == 1:
            return rp_orange_noms["nom"]
        else:
            while repas_orange_moment["midi"] == 0:
                rp_orange_noms = random.choice(repas_orange)
                repas_orange_moment = rp_orange_noms["moment_plat"]
                if repas_orange_moment["midi"] == 1:
                    return rp_orange_noms["nom"]

    elif dail_choice_night[jour] == "repas_orange":
        if repas_orange_moment["soir"] == 1:
            return rp_orange_noms["nom"]
        else:
            while repas_orange_moment["soir"] == 0:
                rp_orange_noms = random.choice(repas_orange)
                repas_orange_moment = rp_orange_noms["moment_plat"]
                if repas_orange_moment["soir"] == 1:
                    return rp_orange_noms["nom"]

def r_vert(jour):
    rp_vert_noms = random.choice(repas_vert)
    repas_vert_moment = rp_vert_noms["moment_plat"]

    if dail_choice_day[jour] == "repas_vert":
        if repas_vert_moment["midi"] == 1:
            return rp_vert_noms["nom"]
        else:
            while repas_vert_moment["midi"] == 0:
                rp_vert_noms = random.choice(repas_vert)
                repas_vert_moment = rp_vert_noms["moment_plat"]
                if repas_vert_moment["midi"] == 1:
                    return rp_vert_noms["nom"]

    elif dail_choice_night[jour] == "repas_vert":
        if repas_vert_moment["soir"] == 1:
            return rp_vert_noms["nom"]
        else:
            while repas_vert_moment["soir"] == 0:
                rp_vert_noms = random.choice(repas_vert)
                repas_vert_moment = rp_vert_noms["moment_plat"]
                if repas_vert_moment["soir"] == 1:
                    return rp_vert_noms["nom"]

jds = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
clr = ["repas_rouge", "repas_jaune", "repas_orange", "repas_vert"]

dail_choice_day = {}
dail_choice_night = {}

for jour in jds:
    dail_choice_day[jour] = None
    dail_choice_night[jour] = None

for jour in jds:
    if jour == "jeudi":
        dail_choice_night[jour] = "Gnocchis/Flamekuch"
        dail_choice_day[jour] = "Riz Cantonnais"
        continue

    if jour == "dimanche":
        dail_choice_day[jour] = "Poulet Rôti"
        dail_choice_night[jour] = "Croque-Monsieur"
        continue

    dail_choice_day[jour] = random.choice(clr)
    dail_choice_night[jour] = random.choice(clr)

    jaune = r_jaune(jour)
    orange = r_orange(jour)
    vert = r_vert(jour)
    rouge = r_rouge(jour)

    if dail_choice_day[jour] == "repas_rouge":
        dail_choice_day[jour] = rouge

    if dail_choice_night[jour] == "repas_rouge":
        dail_choice_night[jour] = rouge

    def combine_meals(meal1, meal2):
        if meal1 and meal2:  # If both are not empty
            return f"{meal1} + {meal2}"
        elif meal1:  # If only meal1 is valid
            return meal1
        elif meal2:  # If only meal2 is valid
            return meal2
        else:
            return "No meal assigned"  # If both are empty

    # Only concatenate non-None meals
    if dail_choice_day[jour] == "repas_rouge" and rouge:
        dail_choice_day[jour] = rouge

    if dail_choice_night[jour] == "repas_rouge" and rouge:
        dail_choice_night[jour] = rouge

    if dail_choice_day[jour] == "repas_jaune":
        dail_choice_day[jour] = combine_meals(jaune, orange)

    if dail_choice_night[jour] == "repas_jaune":
        dail_choice_night[jour] = combine_meals(jaune, orange)

    if dail_choice_day[jour] == "repas_orange":
        dail_choice_day[jour] = combine_meals(orange, vert)

    if dail_choice_night[jour] == "repas_orange":
        dail_choice_night[jour] = combine_meals(orange, vert)

    if dail_choice_day[jour] == "repas_vert":
        dail_choice_day[jour] = combine_meals(vert, jaune)

    if dail_choice_night[jour] == "repas_vert":
        dail_choice_night[jour] = combine_meals(vert, jaune)


@app.route('/api', methods=['GET'])

def api():
    return jsonify({"day": dail_choice_day, "night": dail_choice_night})



if __name__ == '__main__':
    app.run(debug=True, port=8080)