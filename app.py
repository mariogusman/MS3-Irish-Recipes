import os
from types import MethodDescriptorType
from dns.query import receive_udp
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api


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
    Renders main page, Checks user session to display call to action
    Allows users to make searches
    Shows recent recipes added
    """
    # Check user session to show Register call to action
    if session.get("user"):
        logged_in = True
    else:
        logged_in = False

    # returns most recent recipes to show on "recently added"
    recent = list(mongo.db.recipes.find().sort("date", -1))

    # renders index template
    return render_template(
        "index.html", index=index, logged_in=logged_in, recent=recent
    )


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Populates screen with results of query
    Query can come from index.html or the actual search page
    """
    # defines empty variable, if empty an error message will be displayed on the results page
    query = ""
    result = ""
    cat_query = ""
    cat_result = ""

    # gets search content if not empty will search for those terms in Recipes
    query = request.form.get("query")
    if query:
        result = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    # cat_query is for the category icons on homepage
    # will also search for the category in Recipes
    cat_query = request.form.get("cat-query")
    if cat_query:
        cat_result = list(mongo.db.recipes.find({"$text": {"$search": cat_query}}))

    # renders search template
    return render_template("search.html", result=result, cat_result=cat_result)


@app.route("/recipes/<recipe_id>")
def recipes(recipe_id):
    """
    Populates fields with recipe/user data
    """

    # defines recipe and user
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    user = mongo.db.users.find_one({"username": recipe["author"]})

    # returns recipes template
    return render_template("recipes.html", recipe=recipe, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows users to create accounts
    Checks if username is taken
    Pushes new user to the DB
    Logs user in
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # if username taken will display Flash error and 'refresh' page
        if existing_user:
            flash("Oops... This username is already taken!")
            return redirect(url_for("register"))

        # if username not taken and password validated,
        # generates password hash and push to DB
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "youtube": "",
            "instagram": "",
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie and
        # display Flash message Success
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # redirects user to profile page where they can see their recipes and edit profile
        return redirect(url_for("profile", username=session["user"]))
    # Renders register template
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Validates if username is existent and password matches
    """
    if request.method == "POST":
        # Checks if the username exists in Users collection
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # if username exist in Users collection
        if existing_user:
            # Checks if input password matches the one we have and put them in session
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                # redirects to profile page while in session
                return redirect(url_for("profile", username=session["user"]))
            else:
                # If password does not match, display Error message
                # Refreshes login page
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If username does not exist, display Error message
            # Refreshes login page
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    # renders login template
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Allows user to change the profile info and push update to collection
    Alows user to view recipes written by user
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    # if user is logged in
    if session.get("user"):
        if request.method == "POST":
            profile_update = {
                # collects user input in the social media icons
                "user_youtube": request.form.get("user_youtube"),
                "user_instagram": request.form.get("user_instagram").lower(),
            }
            # pushes updated values to the users collection
            mongo.db.users.update_one({"username": username}, {"$set": profile_update})
            # alerts users that profile was updated
            flash("Profile Successfully Updated!")
            # redirects user back to profile page
            return redirect(url_for("profile", username=session["user"]))

        # Retrieve recipes/social links from db added by user
        user_social = mongo.db.users.find_one({"username": username})
        recipes = list(mongo.db.recipes.find({"author": username}).sort("date", -1))
        # renders profile template
        return render_template(
            "profile.html", username=username, recipes=recipes, user_social=user_social
        )

    # if user not logged in - redirects to login page
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
                "photo_url": request.form.get("photo_url"),
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
            new_recipe_update = {
                "title": request.form.get("recipe_title"),
                "description": request.form.get("recipe_description"),
                "category": request.form.get("recipe_category"),
                "time": request.form.get("recipe_time"),
                "yeld": request.form.get("recipe_yeld"),
                "ingredients": request.form.getlist("ingredients"),
                "steps": request.form.getlist("steps"),
                "author": session["user"],
                "date": datetime.datetime.utcnow(),
                "photo_url": request.form.get("photo_url"),
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
    """
    Deletes recipe based on recipe id
    """
    # delete recipe
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    # Flash message success
    flash("Recipe Successfully Deleted!")
    # redirects user back to profile while in session
    return redirect(url_for("profile", username=session["user"]))


@app.route("/logout")
def logout():
    # Removes 'user' from 'session' Cookie
    flash("You have been logged out")
    session.pop("user")
    # redirects user to login page
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=False)
