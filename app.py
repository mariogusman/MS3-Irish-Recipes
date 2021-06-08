import os
from types import MethodDescriptorType
from dns.query import receive_udp
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    """
    Renders main page, Checks user session to display CTA
    Allows users to make searches
    Shows recent recipes added
    """
    # Check user session to show Register CTA
    if session.get("user"):
        logged_in = True
    else:
        logged_in = False

    return render_template("index.html", index=index, logged_in=logged_in)


@app.route("/recipes/<recipe_id>")
def recipes(recipe_id):
    """
    Populates fields with recipe/user data
    """

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    user = mongo.db.users.find_one({"username": recipe["author"]})
    return render_template("recipes.html", recipe=recipe, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Oops... This username is already taken!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "youtube": "",
            "instagram": "",
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks if the username exists in users database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))

                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Allows user to change the profile info and push an update to DB.
    Alows user to view recipes written by user
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    # if  TODOsession["user"]:
    if session.get("user"):
        if request.method == "POST":
            profile_update = {
                "user_youtube": request.form.get("user_youtube"),
                "user_instagram": request.form.get("user_instagram").lower(),
            }
            mongo.db.users.update_one({"username": username}, {"$set": profile_update})
            # alerts users that profile was updated
            flash("Profile Successfully Updated!")
            return redirect(url_for("profile", username=session["user"]))

        # Retrieve recipes from db added by user
        user_social = mongo.db.users.find_one({"username": username})
        recipes = list(mongo.db.recipes.find({"author": username}).sort("date", -1))
        return render_template(
            "profile.html", username=username, recipes=recipes, user_social=user_social
        )

    return redirect(url_for("login"))


@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    """
    Allows users to create recipes and push to DB
    """
    if session.get("user"):
        # If user is logged in
        if request.method == "POST":
            # defines new_recipe using content from the forms
            # uses datetime to get accurate time recipe created
            new_recipe = {
                "title": request.form.get("recipe_title"),
                "description": request.form.get("recipe_description"),
                "category": request.form.get("recipe_category"),
                "time": request.form.get("recipe_time"),
                "yeld": request.form.get("recipe_yeld"),
                "ingredients": request.form.getlist("ingredients"),
                "steps": request.form.getlist("steps"),
                "author": session["user"],
                "date": datetime.datetime.utcnow(),
                "url": request.form.get("recipe_title").replace(" ", "-").lower(),
            }
            # after defining the new object, inserts in the recipes collection
            mongo.db.recipes.insert_one(new_recipe)
            # alerts users that recipe was published
            flash("Recipe Published Successfully!")
            # redirects users to the profile page
            return redirect(url_for("profile", username=session["user"]))

        return render_template("add_recipe.html")

    return redirect(url_for("login"))  # Redirects to login if not logged


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Populates form with recipe old data and,
    allows user to change the values and push an update to DB.
    """
    if session.get("user"):
        # If user is logged in
        if request.method == "POST":
            # defines new_recipe using updated content from the forms
            # date not included to maintain the original date for sorting purposes
            new_recipe_update = {
                "title": request.form.get("recipe_title"),
                "description": request.form.get("recipe_description"),
                "category": request.form.get("recipe_category"),
                "time": request.form.get("recipe_time"),
                "yeld": request.form.get("recipe_yeld"),
                "ingredients": request.form.getlist("ingredients"),
                "steps": request.form.getlist("steps"),
                "author": session["user"],
                "url": request.form.get("recipe_title").replace(" ", "-").lower(),
            }
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, new_recipe_update)
            # alerts users that recipe was published
            flash("Recipe Successfully Updated!")
            # redirects users to the profile page
            return redirect(url_for("profile", username=session["user"]))

        recipe_record = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template("edit_recipe.html", recipe=recipe_record)

    return redirect(url_for("login"))


@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/logout")
def logout():
    # Removes 'user' from 'session' Cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
