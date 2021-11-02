from flask import Blueprint, json, jsonify, request
from flask.helpers import make_response
from app.recipe.Recipe import Recipe
from app import db

recipe_bp = Blueprint("recipes", __name__, url_prefix="/recipes")

@recipe_bp.route("", methods=["POST", "GET"])
def handle_recipes():
    
    if request.method == "POST":

        request_body = request.get_json()

        print(request_body)

        if 'name' not in request_body or 'ingredients' not in request_body:
            return "Missing information in request body", 400

        new_recipe = Recipe(
            name=request_body["name"],
            ingredients=request_body["ingredients"]
        )

        db.session.add(new_recipe)
        db.session.commit()

        return make_response(new_recipe.to_dict(), 201)
    
    elif request.method == "GET":

        recipes = Recipe.query.all()

        return jsonify([recipe.to_dict() for recipe in recipes])

@recipe_bp.route("/<recipe_id>", methods=["GET", "DELETE", "PUT"])
def handle_recipe(recipe_id):

    try:
        int(recipe_id) == recipe_id
    except ValueError:
        return "ID must be an int", 400

    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return f"No recipe with id {recipe_id}", 404
    
    if request.method == "GET":
        return jsonify(recipe.to_dict())
    elif request.method == "DELETE":

        db.session.delete(recipe)
        db.session.commit()

        return f"Recipe with id {recipe_id} deleted."

    elif request.method == "PUT":

        form_info = request.get_json()
        
        if "name" in form_info:
            recipe.name = form_info["name"]
        
        if "ingredients" in form_info:
            recipe.ingredients = form_info["ingredients"]

        db.session.commit()

        return jsonify(recipe.to_dict())
